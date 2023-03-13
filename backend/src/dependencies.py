import pandas as pd
from .settings import *
from .redis_cache import *
import random
import string
import numpy as np
from datetime import datetime
import json
import base64


def decode_payload(payload):
    # Decodificar la cadena base64 del payload
    decoded_payload = base64.b64decode(payload)

    # Convertir la cadena decodificada en un diccionario
    data = json.loads(decoded_payload)

    # Crear un diccionario para almacenar los datos necesarios
    result = {}

    # Extraer los datos necesarios del diccionario
    result['user_id'] = data.get('user_id')
    result['email'] = data.get('email')
    result['expires_at'] = data.get('expires_at')

    return result

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def sql_current_date():
    now = datetime.utcnow()
    now.strftime('%Y-%m-%d %H:%M:%S')
    return now


def run_query(sql):
    try:
        connection = mysql_connect()
        """Runs a given SQL query via the global database connection.

        param sql: MySQL query
        return: Pandas dataframe containing results
        """
        result = pd.read_sql_query(sql, connection)

        result.replace({pd.NaT: None}, inplace=True)

        result.replace({np.nan: None}, inplace=True)

        return result
    except Exception as e:
        import traceback
        print(str(traceback.format_exc()), flush=True)
        connection.close()
        raise Exception('Error en base de datos')


def sql_insert(table: str, columnas: list, valores: list):
    try:
        connection = mysql_connect()
        cursor = connection.cursor()

        if len(columnas) != len(valores):
            raise Exception("Los valores insertados deben ser iguales a las columnas")

        columns = ", ".join(columnas)

        values = '('
        for v in valores:
            values += '%s, '
        values += ')'
        values = values.replace(", )", ")")
        query = f"""
        INSERT INTO `{table}` ({columns})
        VALUES {values}
        """

        connection.ping()
        cursor.execute(query, valores)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        import traceback
        print(str(traceback.format_exc()), flush=True)
        connection.close()
        raise Exception('Error en base de datos')


def sql_update(table: str, columnas: list, valores: list, parametro: str, valor: str):
    try:
        connection = mysql_connect()
        cursor = connection.cursor()

        if len(columnas) != len(valores):
            raise Exception("Los valores insertados deben ser iguales a las columnas")

        update = ''
        for c, v in zip(columnas, valores):
            update += f'{c} = "{v}", '
        update += ')'
        update = update.replace(", )", "").replace('None', 'NULL')
        update = update.replace('"NULL"', "NULL")
        print(update)
        query = f"""
        UPDATE `{table}`
        SET {update}
        WHERE {parametro} = '{valor}'
        """

        connection.ping()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        cursor.close()


def sql_delete(table: str, parametro: str, valor: str):
    try:
        connection = mysql_connect()
        cursor = connection.cursor()

        query = f"""
        DELETE FROM `{table}`
        WHERE {parametro} = '{valor}'
        """

        connection.ping()
        cursor.execute(query)
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        import traceback
        print(str(traceback.format_exc()), flush=True)
        connection.close()
        raise Exception('Error en base de datos')


def sql_search(table: str, parametro='id', valor='all', operator='=', order_by="", columns=[]):
    connection = mysql_connect()
    cursor = connection.cursor()

    if not order_by == "":
        order_by = "ORDER BY " + order_by
    try:
        if not columns:
            if valor == 'all':
                search = run_query(f"SELECT * FROM {table} {order_by}")
            else:
                search = run_query(f"SELECT * FROM {table} WHERE {parametro} {operator} '{valor}' {order_by}")
        else:
            cols = ''
            for i in columns:
                cols += f'{i},'
            cols = cols[:-1]

            if valor == 'all':
                search = run_query(f"SELECT {cols} FROM {table} {order_by}")
            else:
                search = run_query(f"SELECT {cols} FROM {table} WHERE {parametro} {operator} '{valor}' {order_by}")

    except Exception as e:
        search = pd.DataFrame()

    if search.empty:
        found = {}
    else:
        found = search.to_dict('records')

    return found


def sql_search_2_values(table: str,
                        parametro1: str,
                        valor1: str,
                        parametro2: str,
                        valor2: str,
                        operador1='=',
                        operador2='=',
                        order_by="",
                        columns=[],
                        ):
    connection = mysql_connect()
    cursor = connection.cursor()

    if not order_by == "":
        order_by = "ORDER BY " + order_by
    try:
        if not columns:
            search = run_query(f"SELECT * FROM {table} WHERE {parametro1} {operador1} "
                               f"'{valor1}' AND {parametro2} {operador2} '{valor2}' {order_by}")
        else:
            cols = ''
            for i in columns:
                cols += f'{i},'
            cols = cols[:-1]
            search = run_query(f"SELECT {cols} FROM {table} WHERE {parametro1} {operador1} "
                               f"'{valor1}' AND {parametro2} {operador2} '{valor2}' {order_by}")

    except Exception as e:
        search = pd.DataFrame()

    if search.empty:
        found = {}
    else:
        found = search.to_dict('records')

    return found


def sql_count(table: str):
    return int(run_query(f'SELECT COUNT(id) FROM {table};').to_dict('records')[0]['COUNT(id)'])

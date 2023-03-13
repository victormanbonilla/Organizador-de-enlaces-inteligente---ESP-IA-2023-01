import unidecode
import re
import requests
from bs4 import BeautifulSoup
from googletrans import Translator, constants


translator = Translator()

def extraer_texto_web(url):
    # Realizar solicitud a la página web
    response = requests.get(url)
    
    # Extraer el contenido HTML de la página web
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extraer el título de la página web
    titulo = soup.title.string
    
    # Extraer todo el texto de la página web
    texto = soup.get_text()
    
    return titulo, texto

CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

def clean_text(body):
    
    body = cleanhtml(body)
    body = re.sub(r'^https?:\/\/.*[\r\n]*', '', body, flags=re.MULTILINE)
    body = re.sub(r'^http?:\/\/.*[\r\n]*', '', body, flags=re.MULTILINE)

    body= body.lower()
    body = body.strip()
    body= re.sub(r"http\S+", "", body)
    body= re.sub(r"https\S+", "", body)
    body= re.sub(r"www.\S+", "", body)
    body= re.sub("fwd","", body)
    body = body.replace("ñ","n")
    body = body.replace(","," ").replace(";"," ")
    body = body.replace("."," ").replace(";"," ")
    
    
    body = str(body).replace("\n", " ").replace("\r", " ")
    body = str(body).replace("\\n", " ").replace("\\r", " ")
    body = str(body).replace("\\t", " ").replace("xaÂ", "")
    body = str(body).replace("\\xaÂ", "").replace("xaÂ", "")
    body = str(body).replace("xa", "").replace("\\", " ").replace("_"," ")
    body = str(body).replace("xa", "").replace("\\", " ").replace("_"," ")
    body = str(body).replace("Â", "").replace("¡", "").replace("!", "")
    body = str(body).replace("©", "").replace("\t", "")
    body = str(body).replace("Ã³", "").replace("Ã", "")
    body = str(body).replace("±", "").replace("#","")
    body = str(body).replace("-", " ").replace("<", "").replace(">", "")
    body = str(body).replace("[", "").replace("]", "").replace("'", "")
    body = str(body).replace("*", "").replace("Fwd:", "")
    body = str(body).replace("�", "").replace("Forwarded message:", "")
    body = str(body).replace("1", "").replace("6", "")
    body = str(body).replace("2", "").replace("7", "")
    body = str(body).replace("3", "").replace("8", "")
    body = str(body).replace("4", "").replace("9", "")
    body = str(body).replace("5", "").replace("0", "")
    body = str(body).replace("nan", "").replace("¿", "")
    body = str(body).replace("_", " ").replace(":", "")
    body = str(body).replace("lunes", "").replace("miércoles", "")
    body = str(body).replace("martes", "").replace("enero", "")
    body = str(body).replace("miercoles", "").replace("febrero", "")
    body = str(body).replace("jueves", "").replace("marzo", "")
    body = str(body).replace("viernes", "").replace("abril", "")
    body = str(body).replace("mayo", "").replace("septiembre", "")
    body = str(body).replace("junio", "").replace("octubre", "")
    body = str(body).replace("julio", "").replace("noviembre", "")
    body = str(body).replace("agosto", "").replace("diciembre", "")
    
    body = str(body).replace("Enero", "")
    body = str(body).replace("Febrero", "")
    body = str(body).replace("Marzo", "")
    body = str(body).replace("Abil", "")
    
    body = str(body).replace("Mayo", "").replace("Septiembre", "")
    body = str(body).replace("Junio", "").replace("Octubre", "")
    body = str(body).replace("Julio", "").replace("Noviembre", "")
    body = str(body).replace("Agosto", "").replace("Diciembre", "")
    
    body = str(body).replace("rv:", "")
    body = str(body).replace("re:", "").replace("|", " ")
    body = str(body).replace(":", "").replace("*", "")
    body = str(body).replace("ã³", "o").replace("$", "")
    body = str(body).replace("ã", "a").replace("ââ", " ")
    body = str(body).replace("+", " ").replace("y/o", "y")
    body = str(body).replace("\"", "").replace('・', ' ').replace('//', ' ')
    body = str(body).replace("–", "").replace('...', ' ').replace('/', ' ')
    
    body= re.sub("\S*@\S*\s?","", body)
    body = body.replace("ñ","n")
    body = ' '.join(body.split())
    body = unidecode.unidecode(body)
    
    return body
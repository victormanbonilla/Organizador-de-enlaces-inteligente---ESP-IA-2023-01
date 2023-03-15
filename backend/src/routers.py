from fastapi import APIRouter
from fastapi import status as ResponseStatus
from fastapi import Request
from fastapi.encoders import jsonable_encoder
from .auth.oauth2 import *
import traceback
from typing import Union
from fastapi import FastAPI, Header
from datetime import timedelta, datetime

from .redis_cache import *
from .models import *
from .dependencies import *
from .settings import *
from .jwt_decorator import jwt_validation
from .scraping import *
from .ml import *


router = APIRouter()
from .swagger import *


@router.on_event("startup")
async def startup_event():
    db_test = sql_search(table='users', order_by='name')
    redis_set('debug', 'debug')


@router.get("/", response_description="Health check")
async def healthcheck(request: Request, response: Response):
    return {"status": "ok"}


@router.post("/api/auth/register", tags=['Auth'])
async def register(data: Login, response: Response):
    try:
        user = sql_search(
            table='users',
            parametro='user',
            valor=data.user,
            columns=['user'])[0]

    except KeyError:
        user = False

    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User Already Exist",
        )
    else:
        sql_insert(
            'users',
            ['user', 'password'],
            [data.user, data.password]
        )

    return {'success': True}


@router.post("/api/auth/login", tags=['Auth'])
async def login(data: Login, response: Response):
    try:

        user = sql_search(
            table='users',
            parametro='user',
            valor=data.user,
            columns=['user'])[0]

        if not data.password == user['password']:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
            )
        
    except KeyError:
        user = False

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "name":  user['user'],
            "route": "/home"
        },
        expires_delta=access_token_expires
    )

    redis_tem_set(access_token, 60 * 60, access_token)

    return {"token":  access_token}


@router.post("/api/auth/token_validation", response_description="Validacion JSON Web Token", tags=['Auth'])
async def token_validation_external(data: Token, request: Request, response: Response):
    try:
        if check_token(data.token):
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return {"ok": False}

        response_json = {"ok": True}

        return response_json
    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")


@router.post("/api/lists/save_list", response_description="Save user's list", tags=['Backend'])
@jwt_validation
async def save_list(
    data: UserListPayload,
    request: Request,
    response: Response,
    token: Union[str, None] = Header(default='debug')
):
    
    try:
        print(data.data, flush=True)
        data_str = str(json.dumps(jsonable_encoder(data.data)))
        print(data_str, flush=True)
        sql_insert(
            table='lists',
            columnas=['code', 'created_at', 'user_fk', 'data'],
            valores=[
                get_random_string(30),
                sql_current_date(),
                data.user,
                data_str
            ]
        )
        return {'success': True}

    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")


@router.get("/api/lists/share/{list_code}", response_description="Share user's list", tags=['Backend'])
async def share_list(
    request: Request,
    response: Response,
    list_code: str,
):

    try:
        result = sql_search(
            table='lists',
            parametro='code',
            valor=list_code,
            columns=['code', 'data', 'created_at']
        )[0]

        result['data'] = json.loads(result['data'])
        return ResponseModel(result, 'ok')
    except KeyError:
        return ResponseModel([], 'no data was found')
    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        print(str(e), flush=True)
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")


@router.get("/api/lists/get_lists/{user}", response_description="Get user's lists", tags=['Backend'])
@jwt_validation
async def get_lists(
    request: Request,
    response: Response,
    user: str,
    token: Union[str, None] = Header(default=None)
):

    try:
        result = sql_search(
            table='lists',
            parametro='user_fk',
            valor=user,
            columns=['code', 'data', 'created_at'],
            order_by='created_at'
        )

        for i in result:
            i['data'] = json.loads(i['data'])

        return ResponseModel(result, 'ok')
    except KeyError:
        return ResponseModel([], 'no data was found')
    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        print(str(e), flush=True)
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")


@router.post("/api/model/predict", response_description="Predict one URL", tags=['model'])
@jwt_validation
async def get_lists(
    data: PredictModel,
    request: Request,
    response: Response,
    token: Union[str, None] = Header(default=None)
):

    try:
        features = extractor.transform([data.text])
        prediction = model_naive.predict(features)

        prediction = {'Category': categories[int(prediction[0])]}
        return ResponseModel(prediction, 'ok')

    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        print(str(e), flush=True)
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")


@router.post("/api/model/predict_table", response_description="Predict User's Pages", tags=['model'])
@jwt_validation
async def get_lists(
    data: PredictTable,
    request: Request,
    response: Response,
    token: Union[str, None] = Header(default=None)
):

    try:
        results = []
        for url in data.urls:
            
            try:

                title, body = extraer_texto_web(url)
                clean_body = clean_text(body)[:5200]
                text = title + " " + clean_body

                translation = translator.translate(text)
                print(translation, flush=True)

                features = extractor.transform([str(translation.text)])
                prediction = model_naive.predict(features)

                print(prediction, flush=True)
                category = int(prediction[0])

                prediction = {'category': categories[category], 'url': url}

                results.append(prediction)
            except:
                results.append({'category': 'Error', 'url': url})
                
        return ResponseModel(results, 'ok')

    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        print(str(e), flush=True)
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")

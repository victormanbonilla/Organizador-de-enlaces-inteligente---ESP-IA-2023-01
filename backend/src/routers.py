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
router = APIRouter()
from .swagger import *


@router.on_event("startup")
async def startup_event():
    db_test = sql_search(table='users', order_by='name')
    redis_set('debug', 'debug')


@router.get("/", response_description="Health check")
async def healthcheck(request: Request, response: Response):
    return {"status": "ok"}


@router.post("/api/oauth2", tags=['Auth'])
async def oauth2(data: OauthPayload, response: Response):
    try:
        
        oauth_data = decode_payload(data.oauth)
        
        user = sql_search(
            table='users',
            parametro='email',
            valor=oauth_data['email'],
            columns=['name', 'email', 'id_google', 'picture'])[0]
        
        if not user:
            sql_insert(
                table='users',
                columnas=list(oauth_data.keys()),
                valores=list(oauth_data.values()),
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
            "name":  user['name'],
            "picture":  user['picture'],
            "route": "/home"
        },
        expires_delta=access_token_expires
    )
    
    redis_tem_set(access_token, 60 * 60, access_token)

    return {
        "token":  access_token,
        "msg":    "Authentication OK",
        "status": "200"
    }


@router.post("/api/validation", response_description="Validacion JSON Web Token", tags=['Auth'])
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


@router.post("/api/save_list", response_description="Save user's list", tags=['Backend'])
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
            columnas=['code', 'created_at', 'user_id_google', 'data'],
            valores=[
                get_random_string(30), 
                sql_current_date(), 
                data.user_id_google, 
                data_str
                ]
        )
        return {'success': True}
    
    except Exception as e:
        response.status_code = ResponseStatus.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponseModel(str(traceback.format_exc()),
                                  code=500,
                                  message="Error")
        

@router.get("/api/shared_list/{list_code}", response_description="Share user's list", tags=['Backend'])
@jwt_validation
async def share_list(
        request: Request, 
        response: Response,
        list_code: str,
        token: Union[str, None] = Header(default=None)
    ):
                
    try:
        result = sql_search(
            table='lists',
            parametro='code',
            valor=list_code,
            columns=['code', 'data']
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

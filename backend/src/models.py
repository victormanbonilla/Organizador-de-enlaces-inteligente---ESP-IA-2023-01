from typing import Optional, Dict, List
from pydantic import BaseModel
from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm, OAuth2
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request


class EncryptedToken(BaseModel):
    metadata: str

    class Config:
        schema_extra = {
            "example": {
                "metadata": "U2FsdGVkX1/W96QqR27F2NJrjJC38wOKBMg2o1AJ8+"
                            "inPQtJn0s33lBxosOj5ZJxILWCCU3qT0jX7u9cA139d"
                            "JPg8ojOxNeyeU2q/ECXnSQsgKGYUFqTLET9rRkZJtXGdu1"
                            "jJ8YLwptNH4GK9XUk65off2s2beompOtCkypCp/gQVUhSD"
                            "40CN4BaX9lXKiRT10ucIk82U5qHTKhOe2WlIZYm3rlTkvlS"
                            "Ji2EG4Tez5IqMS54/Ij6V8c72qqiW/fG597DnKtQuD+O+bNt"
                            "LAby65vmKuzGZav1Z3txS/QeZwQ=",

            }
        }


class Token(BaseModel):
    token: str

    class Config:
        schema_extra = {
            "example": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                            "eyJ1aWQiOiI2Mjc4OGQ0ZWQ0YzY4ZDZkMDhlZTBhNTYiLCJuYW1lIjoiam9"
                            "yZ2U0IiwiaWF0IjoxNjUyMDY3NjYyLCJleHAiOjE2NTIxNTQwNjJ9.gTv_d"
                            "uJa3cTsq02CeTfjGGdr9Ysp8-cvDQw4mg-c24M",

            }
        }


class OauthPayload(BaseModel):
    token: str

    class Config:
        schema_extra = {
            "example": {
                "token": 'eyJ1c2VyX2lkIjogMSwgImVtYWlsIjogInRlc3RAZXhhbXBsZS5jb20iLCAiZXhwaXJlcyI6ICIyMDIzLTAzLTEzIDIwOjUyOjM0In0=',
            }
        }


class UserListData(BaseModel):
    category: str
    url: str
        
class UserListPayload(BaseModel):
    email: str
    data: List[UserListData]

    class Config:
        schema_extra = {
            "example": {
                'email': 'str',
                'data': [
                    {'category': 'categoria 1', 'url': 'url_1'},
                    {'category': 'categoria 2', 'url': 'url_2'},
                    {'category': 'categoria 3', 'url': 'url_3'},
                ]
            }
        }


class PredictModel(BaseModel):
    text: str

    class Config:
        schema_extra = {
            "example": {
                "text": 'example body',
            }
        }
        

class PredictTable(BaseModel):
    urls: List[str]

    class Config:
        schema_extra = {
            "example": {
                "urls": [
                    'https://url1.com',
                    'https://url2.com',
                    'https://url3.com',
                    ],
            }
        }
             
def ResponseModel(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
  



from fastapi import FastAPI

from src.routers import router

from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

app = FastAPI(
    title="Authentication API",
    description="Api de autenticacion de GrynCar",
    version="1.0",
    openapi_url=None,
    docs_url=None,
    middleware=middleware
)

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8300, host='0.0.0.0')
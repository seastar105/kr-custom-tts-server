from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes.api import router as api_router


def create_app() -> FastAPI:
    application = FastAPI()

    application.mount("/", StaticFiles(directory=".", html=True), name="static")
    # middlewares
    origins = [
        '*'
    ]

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=['*'],
        allow_headers=['*']
    )

    application.include_router(api_router)

    return application


app = create_app()
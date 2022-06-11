from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

from app.api.routes.api import router as api_router


def create_app() -> FastAPI:
    application = FastAPI()

    @application.get("/")
    async def root():
        return FileResponse('index.html')

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
from fastapi import APIRouter

from app.api.routes import tts

router = APIRouter()
router.include_router(tts.router, prefix="/api")
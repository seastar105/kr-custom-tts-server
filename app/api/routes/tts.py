import os
import io
import torch
import scipy.io.wavfile
from fastapi import APIRouter, Response
import numpy as np

from app.schemas.prompt import Prompt
from app.schemas.model import TTSModel
from app.constants import MODEL_PATH, DEVICE

router = APIRouter()
model = None

def synthesize(text: str) -> np.ndarray:
    with torch.no_grad():
        wav = model(text)['wav']
        wav = wav.view(-1).cpu().numpy()
    return wav

def load_model():
    global model
    model_path = None
    if os.path.exists(MODEL_PATH):
        model_path = MODEL_PATH
    model = TTSModel()
    model.load(model_path, DEVICE)

@router.post(
    "/tts",
    responses={
        200: {
            "content": {"audio/wav": {}}
        }
    },
    response_class=Response
)
def TTS(prompt: Prompt):
    global model
    if model is None:
        load_model()
    text = prompt.text
    wav = synthesize(text)
    bytes_wav = bytes()
    bytes_io = io.BytesIO(bytes_wav)
    scipy.io.wavfile.write(bytes_io, model.fs, wav)
    return Response(content=bytes_io.read(), media_type="audio/wave")

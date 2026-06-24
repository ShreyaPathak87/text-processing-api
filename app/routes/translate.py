from fastapi import APIRouter
from app.models.translate_model import TranslateRequest
from app.services.translate_service import translate_text
from app.core.logger import logger

router = APIRouter()

@router.post("/translate")
def translate(request: TranslateRequest):

    logger.info("Translate API called")

    return {
        "translated_text": translate_text(
            request.text,
            request.target_language
        )
    }
from fastapi import APIRouter
from app.models.summarize_model import SummarizeRequest
from app.services.summarize_service import summarize_text
from app.core.logger import logger

router = APIRouter()

@router.post("/summarize")
def summarize(request: SummarizeRequest):

    logger.info("Summarize API called")

    return {
        "summary": summarize_text(request.text)
    }
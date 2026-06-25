from fastapi import APIRouter
from app.models.email_model import EmailRequest
from app.services.email_service import generate_email
from app.core.logger import logger

router = APIRouter()

@router.post("/generate-email")
def email(request: EmailRequest):

    logger.info("Generate Email API called")

    return {
        "email": generate_email(
            request.name,
            request.purpose
        )
    }
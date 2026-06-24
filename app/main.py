from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

import os
from dotenv import load_dotenv

from app.routes import summarize, translate, email_generator
from app.core.logger import logger

# Load environment variables
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Text Processing API")
DEBUG = os.getenv("DEBUG", "True")

# Initialize FastAPI app
app = FastAPI(title=APP_NAME)

# Log app startup
logger.info("🚀 App started successfully")

# Include routers
app.include_router(summarize.router)
app.include_router(translate.router)
app.include_router(email_generator.router)


# Home route
@app.get("/")
def home():
    return {
        "message": "API Running Successfully",
        "app_name": APP_NAME,
        "debug": DEBUG
    }


# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Error occurred: {str(exc)}")

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong. Please try again later."
        }
    )
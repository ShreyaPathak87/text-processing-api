import logging
import os

# ensure logs folder exists
os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("text_api_logger")
logger.setLevel(logging.INFO)

# prevent duplicate handlers
if not logger.handlers:

    file_handler = logging.FileHandler("logs/app.log")

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
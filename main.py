import logging

from fastapi import FastAPI
import uvicorn
from core.config import settings
from common_logger.logger_config import configure_logger

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/")
async def root_page():
    return {"message": "Hello World"}


if __name__ == "__main__":
    configure_logger(level=logging.INFO)
    logger.info("Starting FastAPI app")
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
    logger.info("FastAPI app stopped")

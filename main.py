import logging

from fastapi import FastAPI
import uvicorn
from core.config import settings
from common_logger.logger_config import configure_logger

logger = logging.getLogger(__name__)

app = FastAPI()


# some comment
@app.get("/")
async def root_page():
    return {"message": "Hello World"}


@app.get("/user")
async def get_user():
    return {
        "id": "16fc42b4ac60aa4d31ef7a8bdee7903ac",
        "username": "Random",
        "email": "random@example.com",
    }


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

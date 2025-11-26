# logging_system.py
import logging
from pathlib import Path

LOG_FILE = Path("data/app.log")

def setup_logging(level: str = "INFO"):
    LOG_FILE.parent.mkdir(exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )

    logging.info(f"Logging initialized with level: {level}")

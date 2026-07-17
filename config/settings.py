from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
LOG_DIR = BASE_DIR / "logs"

RAW_DATA_FILE = RAW_DATA_DIR / os.getenv("DATA_FILE")

# Spark Configuration

APP_NAME = os.getenv("APP_NAME")
MASTER = os.getenv("MASTER")
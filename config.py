import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

ombd_api_key = os.getenv("OMBD_API_KEY")

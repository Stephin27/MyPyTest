import os
from pathlib import Path

class Config:
    # Base Paths
    PROJECT_ROOT = Path(__file__).parent
    DATA_DIR = PROJECT_ROOT / "data"
    REPORTS_DIR = PROJECT_ROOT / "reports"
    LOGS_DIR = PROJECT_ROOT / "logs"

    # URLs
    BASE_URL = "https://rahulshettyacademy.com/AutomationPractice/"

    # Execution Settings
    TIMEOUT = 10000  # 10 seconds in milliseconds
    LOG_LEVEL = "INFO"

    # Ensure directories exist
    DATA_DIR.mkdir(exist_ok=True)
    REPORTS_DIR.mkdir(exist_ok=True)
    LOGS_DIR.mkdir(exist_ok=True)

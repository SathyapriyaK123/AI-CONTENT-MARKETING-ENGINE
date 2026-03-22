"""
Logging configuration
"""
import logging
import sys
from datetime import datetime


def setup_logging(log_level: str = "INFO"):
    """
    Configure application logging
    
    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR)
    """
    # Create logs directory if it doesn't exist
    import os
    if not os.path.exists("logs"):
        os.makedirs("logs")
    
    # Log file with timestamp
    log_file = f"logs/app_{datetime.now().strftime('%Y%m%d')}.log"
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # File handler
            logging.FileHandler(log_file),
            # Console handler
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Set specific loggers
    logging.getLogger("app").setLevel(logging.INFO)
    logging.getLogger("celery").setLevel(logging.WARNING)
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    
    return logging.getLogger(__name__)


def get_logger(name: str):
    """Get logger for specific module"""
    return logging.getLogger(name)
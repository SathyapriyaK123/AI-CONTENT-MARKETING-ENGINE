import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    
    # App Settings
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    PROJECT_NAME: str = "AI Content Marketing Engine"
    VERSION: str = "1.0.0"
    
    # Content Generation Limits
    MIN_WORD_COUNT: int = 50
    MAX_WORD_COUNT: int = 2000
    DEFAULT_WORD_COUNT: int = 500
    
    # API Rate Limiting
    MAX_RETRIES: int = 3
    RETRY_DELAY: float = 2.0
    BACKOFF_FACTOR: float = 2.0
    
    # Task Queue Settings
    CELERY_TASK_TIME_LIMIT: int = 300  # 5 minutes
    CELERY_RESULT_EXPIRES: int = 3600  # 1 hour
    
    # Content Quality
    MIN_READABILITY_SCORE: float = 30.0
    TARGET_READABILITY_SCORE: float = 60.0
    
    # Supported Options
    VALID_TONES: list = ["professional", "casual", "funny", "formal", "persuasive"]
    VALID_INDUSTRIES: list = ["tech", "fashion", "health", "food", "finance", "education", "ecommerce", "real_estate"]
    
    def validate(self):
        """Validate configuration"""
        if not self.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return True

settings = Settings()
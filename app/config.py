import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    
    # Project metadata
    PROJECT_NAME: str = "AI Content Marketing Engine"
    VERSION: str = "0.1.0"
    
    def validate(self):
        """Validate critical configuration"""
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        return True

settings = Settings()
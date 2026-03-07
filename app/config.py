import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings and configuration"""
    
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    DEBUG: bool = os.getenv("DEBUG", "True") == "True"
    
    # Project metadata
    PROJECT_NAME: str = "AI Content Marketing Engine"
    VERSION: str = "0.2.0"
    
    def validate(self):
        """Validate critical configuration"""
        if not self.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return True

settings = Settings()
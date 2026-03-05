from fastapi import FastAPI
from app.config import settings

# Validate configuration on startup
settings.validate()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

@app.get("/")
def root():
    """Root endpoint - health check"""
    return {
        "message": "AI Content Marketing Engine API",
        "version": settings.VERSION,
        "status": "operational"
    }

@app.get("/health")
def health_check():
    """Detailed health check endpoint"""
    return {
        "status": "healthy",
        "openai_configured": bool(settings.OPENAI_API_KEY),
        "redis_url": settings.REDIS_URL
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
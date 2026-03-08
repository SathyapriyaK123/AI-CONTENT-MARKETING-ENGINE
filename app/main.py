from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.services.text_generator import (
    generate_blog_post,
    generate_tweets,
    generate_instagram_caption,
    generate_linkedin_post,
    generate_email_marketing,
    generate_product_description
)# Validate configuration on startup
settings.validate()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    description="Multi-modal AI content marketing engine powered by Groq"
)


# Request models
class CampaignRequest(BaseModel):
    campaign_brief: str
    word_count: int = 500


class TweetRequest(BaseModel):
    campaign_brief: str
    count: int = 3


# Root endpoints
@app.get("/")
def root():
    """Root endpoint - API information"""
    return {
        "message": "AI Content Marketing Engine API",
        "version": settings.VERSION,
        "status": "operational",
        "powered_by": "Groq (FREE & FAST)",
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "generate_blog": "/generate/blog",
            "generate_tweets": "/generate/tweets",
            "generate_instagram": "/generate/instagram",
            "generate_campaign": "/generate/campaign"
        }
    }


@app.get("/health")
def health_check():
    """Detailed health check endpoint"""
    return {
        "status": "healthy",
        "groq_configured": bool(settings.GROQ_API_KEY),
        "version": settings.VERSION
    }


# Content generation endpoints
@app.post("/generate/blog")
def create_blog(request: CampaignRequest):
    """Generate a professional blog post"""
    try:
        blog_post = generate_blog_post(
            campaign_brief=request.campaign_brief,
            word_count=request.word_count
        )
        
        return {
            "success": True,
            "campaign_brief": request.campaign_brief,
            "word_count": request.word_count,
            "blog_post": blog_post,
            "actual_word_count": len(blog_post.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/tweets")
def create_tweets(request: TweetRequest):
    """Generate multiple tweet variants"""
    try:
        tweets = generate_tweets(
            campaign_brief=request.campaign_brief,
            count=request.count
        )
        
        return {
            "success": True,
            "campaign_brief": request.campaign_brief,
            "count": len(tweets),
            "tweets": tweets
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/instagram")
def create_instagram_caption(campaign_brief: str):
    """Generate Instagram caption with hashtags"""
    try:
        caption = generate_instagram_caption(campaign_brief)
        
        return {
            "success": True,
            "campaign_brief": campaign_brief,
            "caption": caption,
            "character_count": len(caption)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/campaign")
def create_full_campaign(request: CampaignRequest):
    """Generate complete marketing campaign"""
    try:
        blog = generate_blog_post(request.campaign_brief, request.word_count)
        tweets = generate_tweets(request.campaign_brief, count=3)
        instagram = generate_instagram_caption(request.campaign_brief)
        
        return {
            "success": True,
            "campaign_brief": request.campaign_brief,
            "content": {
                "blog_post": blog,
                "tweets": tweets,
                "instagram_caption": instagram
            },
            "summary": {
                "blog_word_count": len(blog.split()),
                "tweet_count": len(tweets),
                "instagram_char_count": len(instagram)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


@app.post("/generate/linkedin")
def create_linkedin_post(campaign_brief: str):
    """Generate professional LinkedIn post"""
    try:
        post = generate_linkedin_post(campaign_brief)
        
        return {
            "success": True,
            "campaign_brief": campaign_brief,
            "linkedin_post": post,
            "word_count": len(post.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.post("/generate/email")
def create_email(campaign_brief: str, email_type: str = "promotional"):
    """
    Generate email marketing copy
    
    - **campaign_brief**: Product/campaign description
    - **email_type**: Type of email (promotional, welcome, newsletter, etc.)
    """
    try:
        email = generate_email_marketing(campaign_brief, email_type)
        
        return {
            "success": True,
            "campaign_brief": campaign_brief,
            "email_type": email_type,
            "email_content": email,
            "word_count": len(email.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/product-description")
def create_product_description(product_name: str, features: str = ""):
    """
    Generate compelling product description
    
    - **product_name**: Name of the product
    - **features**: Optional key features (comma-separated)
    """
    try:
        description = generate_product_description(product_name, features)
        
        return {
            "success": True,
            "product_name": product_name,
            "features": features,
            "description": description,
            "word_count": len(description.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
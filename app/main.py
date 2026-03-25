from app.services.seo_generator import generate_seo_package
from app.services.content_quality import extract_keywords, extract_hashtags
from fastapi import FastAPI, HTTPException
from app.services.content_quality import analyze_content_quality
from pydantic import BaseModel
from app.config import settings
from app.services.text_generator import (
    generate_blog_post,
    generate_tweets,
    generate_instagram_caption,
    generate_linkedin_post,
    generate_email_marketing,
    generate_product_description,
    generate_industry_blog
)
from app.services.content_templates import get_available_industries, validate_industryfrom app.api.async_endpoints import router as async_router

# Validate configuration on startup
settings.validate()

app = FastAPI(
# Serve frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    description="Multi-modal AI content marketing engine powered by Groq"
)

# Include async routes
app.include_router(async_router)


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
        "features": {
            "sync_endpoints": "Direct generation",
            "async_endpoints": "Background processing with Celery"
        },
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "sync_generate": "/generate/*",
            "async_generate": "/async/generate/*"
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


# Synchronous content generation endpoints
@app.post("/generate/blog")
def create_blog(request: CampaignRequest):
    """Generate a professional blog post (synchronous)"""
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
@app.post("/generate/blog")
def create_blog(request: CampaignRequest, tone: str = "professional"):
    """
    Generate a professional blog post (synchronous)
    
    - **tone**: professional, casual, funny, formal, persuasive
    """
    try:
        # Validate tone
        valid_tones = ["professional", "casual", "funny", "formal", "persuasive"]
        if tone not in valid_tones:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid tone. Choose from: {', '.join(valid_tones)}"
            )
        
        blog_post = generate_blog_post(
            campaign_brief=request.campaign_brief,
            word_count=request.word_count,
            tone=tone
        )
        
        return {
            "success": True,
            "campaign_brief": request.campaign_brief,
            "word_count": request.word_count,
            "tone": tone,
            "blog_post": blog_post,
            "actual_word_count": len(blog_post.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/tweets")
def create_tweets(request: TweetRequest):
    """Generate multiple tweet variants (synchronous)"""
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
    """Generate Instagram caption with hashtags (synchronous)"""
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


@app.post("/generate/linkedin")
def create_linkedin_post(campaign_brief: str):
    """Generate professional LinkedIn post (synchronous)"""
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
@app.post("/generate/linkedin")
def create_linkedin_post(campaign_brief: str, tone: str = "professional"):
    """
    Generate professional LinkedIn post (synchronous)
    
    - **tone**: professional, casual, inspirational, thought_leadership
    """
    try:
        valid_tones = ["professional", "casual", "inspirational", "thought_leadership"]
        if tone not in valid_tones:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid tone. Choose from: {', '.join(valid_tones)}"
            )
        
        post = generate_linkedin_post(campaign_brief, tone)
        
        return {
            "success": True,
            "campaign_brief": campaign_brief,
            "tone": tone,
            "linkedin_post": post,
            "word_count": len(post.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate/email")
def create_email(campaign_brief: str, email_type: str = "promotional"):
    """Generate email marketing copy (synchronous)"""
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
    """Generate compelling product description (synchronous)"""
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


@app.post("/generate/campaign")
def create_full_campaign(request: CampaignRequest):
    """Generate complete marketing campaign (synchronous)"""
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
@app.post("/generate/industry-blog")
def create_industry_blog(
    request: CampaignRequest,
    industry: str,
    tone: str = "professional"
):
    """
    Generate blog post optimized for specific industry
    
    - **industry**: tech, fashion, health, food, finance, education, ecommerce, real_estate
    - **tone**: professional, casual, funny, formal, persuasive
    """
    try:
        # Validate industry
        if not validate_industry(industry):
            available = get_available_industries()
            raise HTTPException(
                status_code=400,
                detail=f"Invalid industry. Choose from: {', '.join(available)}"
            )
        
        # Validate tone
        valid_tones = ["professional", "casual", "funny", "formal", "persuasive"]
        if tone not in valid_tones:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid tone. Choose from: {', '.join(valid_tones)}"
            )
        
        blog_post = generate_industry_blog(
            campaign_brief=request.campaign_brief,
            industry=industry,
            word_count=request.word_count,
            tone=tone
        )
        
        return {
            "success": True,
            "campaign_brief": request.campaign_brief,
            "industry": industry,
            "tone": tone,
            "word_count": request.word_count,
            "blog_post": blog_post,
            "actual_word_count": len(blog_post.split())
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/industries")
def list_industries():
    """Get list of available industry templates"""
    industries = get_available_industries()
    return {
        "success": True,
        "count": len(industries),
        "industries": industries
    }
@app.post("/analyze/quality")
def analyze_quality(text: str, target_word_count: int = None):
    """
    Analyze content quality
    Returns readability score, word count validation, and metrics
    """
    try:
        analysis = analyze_content_quality(text, target_word_count)
        
        return {
            "success": True,
            "analysis": analysis
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
@app.post("/generate/seo")
def generate_seo_metadata(text: str, campaign_brief: str):
    """
    Generate SEO metadata package
    Returns title tag, meta description, keywords, URL slug
    """
    try:
        seo = generate_seo_package(text, campaign_brief)
        return {
            "success": True,
            "seo": seo
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/extract/keywords")
def get_keywords(text: str, max_keywords: int = 10):
    """Extract important keywords from text"""
    try:
        keywords = extract_keywords(text, max_keywords)
        hashtags = extract_hashtags(text, 5)
        
        return {
            "success": True,
            "keywords": keywords,
            "hashtags": hashtags
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
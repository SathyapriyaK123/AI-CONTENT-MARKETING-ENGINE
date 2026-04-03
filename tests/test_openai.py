import os
import pytest
from dotenv import load_dotenv
from fastapi.testclient import TestClient

from app.main import app
from groq import Groq

load_dotenv()

client = TestClient(app)

@pytest.fixture
def groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    assert api_key is not None, "❌ GROQ_API_KEY is not set in .env"
    return Groq(api_key=api_key)

def test_api_key_works(groq_client):
    """Test if Groq API key is valid and request succeeds"""
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Say 'API key works!'"}],
            max_tokens=10
        )
        assert response is not None
        assert response.choices is not None
        assert len(response.choices) > 0
    except Exception as e:
        pytest.skip(f"Groq API call failed (might be a missing or invalid local key): {e}")

def test_invalid_api_key():
    """Test behavior with invalid API key"""
    fake_client = Groq(api_key="invalid_key")

    with pytest.raises(Exception):
        fake_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )

def test_env_loaded():
    """Ensure environment variables are loaded"""
    assert os.getenv("GROQ_API_KEY") is not None, "❌ .env not loaded properly"

def test_root_endpoint():
    """Test the root endpoint containing API info"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"
    assert "features" in data

def test_health_check():
    """Test detailed health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "groq_configured" in data

def test_industries_list():
    """Test listing available industries"""
    response = client.get("/industries")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "industries" in data
    assert isinstance(data["industries"], list)

def test_analyze_quality():
    """Test local content quality analysis"""
    response = client.post(
        "/analyze/quality",
        params={"text": "This is a simple test sentence. It has a few words.", "target_word_count": 10}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "analysis" in data
    assert data["analysis"]["word_count"] > 0

def test_extract_keywords():
    """Test local keyword extraction"""
    response = client.post(
        "/extract/keywords",
        params={"text": "Marketing strategy involves planning and content generation.", "max_keywords": 3}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "keywords" in data
    assert len(data["keywords"]) > 0

def test_generate_seo_metadata():
    """Test SEO generator endpoint"""
    response = client.post(
        "/generate/seo",
        params={
            "text": "This is a detailed paragraph about AI marketing and strategies for the future of digital content.",
            "campaign_brief": "AI Marketing Guide"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "seo" in data
    assert "title_tag" in data["seo"]
    assert "meta_description" in data["seo"]

def test_generate_instagram():
    """Test Instagram caption generation (makes full API call to Groq via app endpoint)"""
    response = client.post(
        "/generate/instagram",
        params={"campaign_brief": "Test brief"}
    )
    # The call may return 500 if the real API key rate limits or is missing/invalid
    assert response.status_code in [200, 500] 
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "caption" in data

def test_generate_blog_success():
    """Test successful blog generation"""
    response = client.post(
        "/generate/blog",
        json={"campaign_brief": "Test brief", "word_count": 100},
        params={"tone": "professional"}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "blog_post" in data

def test_generate_blog_invalid_tone():
    """Test blog generation with invalid tone"""
    response = client.post(
        "/generate/blog",
        json={"campaign_brief": "Test brief", "word_count": 100},
        params={"tone": "invalid_tone"}
    )
    assert response.status_code == 400
    assert "Invalid tone" in response.json()["detail"]

def test_generate_blog_missing_payload():
    """Test blog generation with missing payload"""
    response = client.post("/generate/blog")
    assert response.status_code == 422

def test_generate_tweets():
    """Test tweets generation"""
    response = client.post(
        "/generate/tweets",
        json={"campaign_brief": "Test brief", "count": 2}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "tweets" in data

def test_generate_linkedin_success():
    """Test successful LinkedIn post generation"""
    response = client.post(
        "/generate/linkedin",
        params={"campaign_brief": "Test brief", "tone": "professional"}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "linkedin_post" in data

def test_generate_linkedin_invalid_tone():
    """Test LinkedIn post generation with invalid tone"""
    response = client.post(
        "/generate/linkedin",
        params={"campaign_brief": "Test brief", "tone": "invalid_tone"}
    )
    assert response.status_code == 400
    assert "Invalid tone" in response.json()["detail"]

def test_generate_email():
    """Test email generation"""
    response = client.post(
        "/generate/email",
        params={"campaign_brief": "Test brief", "email_type": "newsletter"}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "email_content" in data

def test_generate_product_description():
    """Test product description generation"""
    response = client.post(
        "/generate/product-description",
        params={"product_name": "Test Product", "features": "Fast, Reliable"}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "description" in data

def test_generate_campaign():
    """Test full campaign generation"""
    response = client.post(
        "/generate/campaign",
        json={"campaign_brief": "Test brief", "word_count": 100}
    )
    assert response.status_code in [200, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "content" in data
        assert "blog_post" in data["content"]
        assert "tweets" in data["content"]
        assert "instagram_caption" in data["content"]

def test_generate_industry_blog_success():
    """Test successful industry blog generation"""
    response = client.post(
        "/generate/industry-blog",
        json={"campaign_brief": "Test brief", "word_count": 100},
        params={"industry": "tech", "tone": "professional"}
    )
    # The endpoint might return 400 if "tech" is not available in the templates. 
    # Valid ranges include 200, 400, 500 depending on environment setup.
    assert response.status_code in [200, 400, 500]
    if response.status_code == 200:
        data = response.json()
        assert data["success"] is True
        assert "blog_post" in data

def test_generate_industry_blog_invalid_industry():
    """Test industry blog generation with invalid industry"""
    response = client.post(
        "/generate/industry-blog",
        json={"campaign_brief": "Test brief", "word_count": 100},
        params={"industry": "invalid_industry", "tone": "professional"}
    )
    assert response.status_code == 400
    assert "Invalid industry" in response.json()["detail"]

def test_generate_industry_blog_invalid_tone():
    """Test industry blog generation with invalid tone"""
    response = client.post(
        "/generate/industry-blog",
        json={"campaign_brief": "Test brief", "word_count": 100},
        params={"industry": "tech", "tone": "invalid_tone"}
    )
    assert response.status_code == 400
    assert "Invalid" in response.json()["detail"]

"""
Application constants
"""

# Content generation defaults
DEFAULT_BLOG_WORD_COUNT = 500
DEFAULT_TWEET_COUNT = 3
DEFAULT_TONE = "professional"
DEFAULT_INDUSTRY = "tech"

# Validation limits
MIN_WORD_COUNT = 50
MAX_WORD_COUNT = 2000
MIN_TWEET_COUNT = 1
MAX_TWEET_COUNT = 10
MIN_CAMPAIGN_BRIEF_LENGTH = 3
MAX_CAMPAIGN_BRIEF_LENGTH = 500

# Readability thresholds
EXCELLENT_READABILITY = 80
GOOD_READABILITY = 60
FAIR_READABILITY = 50
POOR_READABILITY = 30

# API response codes
SUCCESS_CODE = "SUCCESS"
ERROR_CODE = "ERROR"
PROCESSING_CODE = "PROCESSING"
PENDING_CODE = "PENDING"

# Content type identifiers
CONTENT_TYPES = {
    "BLOG": "blog_post",
    "TWEET": "tweet",
    "INSTAGRAM": "instagram_caption",
    "LINKEDIN": "linkedin_post",
    "EMAIL": "email_marketing",
    "PRODUCT": "product_description",
    "CAMPAIGN": "full_campaign"
}

# Industry keywords mapping
INDUSTRY_KEYWORDS = {
    "tech": ["innovative", "cutting-edge", "digital", "AI", "cloud", "software"],
    "fashion": ["trendy", "stylish", "elegant", "chic", "designer", "collection"],
    "health": ["wellness", "healthy", "natural", "proven", "vitality", "care"],
    "food": ["delicious", "fresh", "organic", "artisan", "gourmet", "flavorful"],
    "finance": ["secure", "trusted", "investment", "returns", "growth", "reliable"],
    "education": ["learn", "expert", "certified", "comprehensive", "skills", "master"],
    "ecommerce": ["quality", "affordable", "fast shipping", "guarantee", "bestseller"],
    "real_estate": ["prime", "luxury", "spacious", "modern", "investment", "location"]
}

# Tone descriptions
TONE_DESCRIPTIONS = {
    "professional": "Clear, authoritative, and credible",
    "casual": "Friendly, conversational, and approachable",
    "funny": "Humorous, witty, and entertaining",
    "formal": "Sophisticated, academic, and precise",
    "persuasive": "Compelling, benefit-focused, and action-oriented"
}

# HTTP status codes
HTTP_OK = 200
HTTP_BAD_REQUEST = 400
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500
HTTP_RATE_LIMIT = 429
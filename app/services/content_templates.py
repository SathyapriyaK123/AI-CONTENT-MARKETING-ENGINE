
Text generation services using Groq AI

This module provides functions for generating various types of marketing content
including blog posts, tweets, social media captions, and more.

Functions:
    generate_blog_post: Create professional blog posts with tone control
    generate_tweets: Generate multiple tweet variants
    generate_instagram_caption: Create Instagram captions with hashtags
    generate_linkedin_post: Professional LinkedIn content
    generate_email_marketing: Email marketing copy
    generate_product_description: Product descriptions
    generate_industry_blog: Industry-specific blog posts
"""
Industry-specific content templates
Pre-configured prompts for different industries
"""

INDUSTRY_TEMPLATES = {
    "tech": {
        "focus": "innovation, features, technical benefits, efficiency",
        "keywords": ["cutting-edge", "innovative", "streamlined", "powerful", "solution"],
        "tone": "professional and forward-thinking",
        "examples": "software, apps, AI, cloud services, automation tools"
    },
    "fashion": {
        "focus": "style, trends, aesthetics, lifestyle, self-expression",
        "keywords": ["trendy", "stylish", "elegant", "chic", "timeless"],
        "tone": "aspirational and vibrant",
        "examples": "clothing, accessories, sustainable fashion, luxury brands"
    },
    "health": {
        "focus": "wellness, benefits, safety, science-backed claims",
        "keywords": ["healthy", "natural", "proven", "wellness", "vitality"],
        "tone": "trustworthy and informative",
        "examples": "supplements, fitness, nutrition, mental health, medical devices"
    },
    "food": {
        "focus": "taste, quality, ingredients, experience, sustainability",
        "keywords": ["delicious", "fresh", "artisan", "organic", "flavorful"],
        "tone": "appetizing and inviting",
        "examples": "restaurants, food products, recipes, meal delivery, beverages"
    },
    "finance": {
        "focus": "security, returns, trust, expertise, compliance",
        "keywords": ["secure", "profitable", "trusted", "expert", "guaranteed"],
        "tone": "authoritative and reassuring",
        "examples": "banking, investments, insurance, fintech, financial planning"
    },
    "education": {
        "focus": "learning outcomes, expertise, accessibility, value",
        "keywords": ["learn", "master", "expert-led", "comprehensive", "certified"],
        "tone": "encouraging and knowledgeable",
        "examples": "courses, tutoring, e-learning platforms, schools, training"
    },
    "ecommerce": {
        "focus": "value, convenience, quality, customer satisfaction",
        "keywords": ["affordable", "fast shipping", "quality", "guarantee", "bestseller"],
        "tone": "persuasive and customer-focused",
        "examples": "online stores, marketplaces, dropshipping, retail"
    },
    "real_estate": {
        "focus": "location, investment, lifestyle, features, opportunity",
        "keywords": ["prime location", "investment", "spacious", "modern", "exclusive"],
        "tone": "aspirational and detailed",
        "examples": "properties, rentals, commercial real estate, property management"
    }
}


def get_industry_prompt_enhancement(industry: str) -> str:
    """
    Get industry-specific prompt enhancement
    
    Args:
        industry: Industry category (tech, fashion, health, etc.)
    
    Returns:
        Enhanced prompt instructions for that industry
    """
    if industry not in INDUSTRY_TEMPLATES:
        return ""
    
    template = INDUSTRY_TEMPLATES[industry]
    
    enhancement = f"""
INDUSTRY FOCUS: {industry.upper()}

Key Focus Areas: {template['focus']}
Recommended Keywords: {', '.join(template['keywords'])}
Writing Tone: {template['tone']}

Example Products/Services: {template['examples']}

Write in a way that resonates with {industry} industry audiences.
"""
    return enhancement


def get_available_industries():
    """Get list of available industry templates"""
    return list(INDUSTRY_TEMPLATES.keys())


def validate_industry(industry: str) -> bool:
    """Check if industry template exists"""
    return industry in INDUSTRY_TEMPLATES
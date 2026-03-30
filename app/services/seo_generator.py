from app.services.content_quality import extract_keywords


def generate_meta_description(text: str, max_length: int = 160) -> str:
    """
    Generate SEO meta description from text
    Optimized for search engines (160 chars max)
    """
    # Get first paragraph or sentences
    sentences = text.split('.')
    
    description = ""
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            if len(description + sentence) < max_length - 3:
                description += sentence + ". "
            else:
                break
    
    # Trim to max length
    description = description.strip()[:max_length]
    
    # Remove incomplete sentence at end
    if not description.endswith('.'):
        last_period = description.rfind('.')
        if last_period > 0:
            description = description[:last_period + 1]
    
    return description.strip()


def generate_title_tag(campaign_brief: str, max_length: int = 60) -> str:
    """
    Generate SEO title tag
    Optimized for search engines (60 chars max)
    """
    # Capitalize important words
    words = campaign_brief.split()
    title_words = [word.capitalize() for word in words]
    title = ' '.join(title_words)
    
    # Add benefit/hook if space allows
    if len(title) < 40:
        title += " | Benefits & Guide"
    
    # Trim to max length
    return title[:max_length]


def generate_seo_package(text: str, campaign_brief: str) -> dict:
    """
    Generate complete SEO package
    """
    keywords = extract_keywords(text, 10)
    
    return {
        "title_tag": generate_title_tag(campaign_brief),
        "meta_description": generate_meta_description(text),
        "keywords": keywords[:5],
        "focus_keyword": keywords[0] if keywords else campaign_brief.split()[0],
        "url_slug": campaign_brief.lower().replace(' ', '-')[:50]
    }
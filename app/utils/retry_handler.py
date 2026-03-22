"""
Input validation utilities
"""
from app.utils.error_messages import format_validation_error


def validate_word_count(word_count: int) -> dict:
    """Validate word count is reasonable"""
    if word_count < 50:
        return format_validation_error("word_count", "Minimum word count is 50")
    if word_count > 2000:
        return format_validation_error("word_count", "Maximum word count is 2000")
    return {"valid": True}


def validate_campaign_brief(brief: str) -> dict:
    """Validate campaign brief"""
    if not brief or not brief.strip():
        return format_validation_error("campaign_brief", "Campaign brief cannot be empty")
    if len(brief) < 3:
        return format_validation_error("campaign_brief", "Campaign brief too short (min 3 characters)")
    if len(brief) > 500:
        return format_validation_error("campaign_brief", "Campaign brief too long (max 500 characters)")
    return {"valid": True}


def validate_tone(tone: str, valid_tones: list) -> dict:
    """Validate tone parameter"""
    if tone not in valid_tones:
        return format_validation_error(
            "tone",
            f"Invalid tone '{tone}'. Choose from: {', '.join(valid_tones)}"
        )
    return {"valid": True}


def validate_industry(industry: str, valid_industries: list) -> dict:
    """Validate industry parameter"""
    if industry not in valid_industries:
        return format_validation_error(
            "industry",
            f"Invalid industry '{industry}'. Choose from: {', '.join(valid_industries)}"
        )
    return {"valid": True}


def validate_count(count: int, min_count: int = 1, max_count: int = 10) -> dict:
    """Validate count parameter"""
    if count < min_count:
        return format_validation_error("count", f"Minimum count is {min_count}")
    if count > max_count:
        return format_validation_error("count", f"Maximum count is {max_count}")
    return {"valid": True}
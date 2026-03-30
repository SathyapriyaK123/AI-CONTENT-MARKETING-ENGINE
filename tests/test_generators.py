"""
Tests for content generators
"""
import pytest
from app.services.text_generator import generate_blog_post, generate_tweets

def test_blog_generation():
    """Test blog post generation"""
    result = generate_blog_post("test product", 100, "professional")
    assert isinstance(result, str)
    assert len(result) > 0

def test_tweet_generation():
    """Test tweet generation"""
    result = generate_tweets("test product", 2)
    assert isinstance(result, list)
    assert len(result) == 2
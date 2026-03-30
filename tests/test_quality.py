"""
Tests for content quality analysis
"""
import pytest
from app.services.content_quality import (
    count_words,
    calculate_readability,
    validate_word_count
)

def test_word_count():
    """Test word counting"""
    text = "This is a test"
    assert count_words(text) == 4

def test_readability():
    """Test readability calculation"""
    text = "This is a simple sentence."
    result = calculate_readability(text)
    assert "flesch_score" in result
    assert "readability" in result

def test_word_count_validation():
    """Test word count validation"""
    result = validate_word_count("word " * 100, 100)
    assert result["valid"] == True
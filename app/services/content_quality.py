"""
Content quality validation and scoring
"""
import re
from typing import Dict


def count_words(text: str) -> int:
    """Count words in text"""
    return len(text.split())


def count_sentences(text: str) -> int:
    """Count sentences in text"""
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])


def count_syllables(word: str) -> int:
    """Estimate syllables in a word"""
    word = word.lower()
    vowels = 'aeiouy'
    syllable_count = 0
    previous_was_vowel = False
    
    for char in word:
        is_vowel = char in vowels
        if is_vowel and not previous_was_vowel:
            syllable_count += 1
        previous_was_vowel = is_vowel
    
    # Adjust for silent 'e'
    if word.endswith('e'):
        syllable_count -= 1
    
    # Minimum one syllable
    if syllable_count == 0:
        syllable_count = 1
    
    return syllable_count


def calculate_readability(text: str) -> Dict[str, float]:
    """
    Calculate readability scores
    Returns Flesch Reading Ease and Grade Level
    """
    words = count_words(text)
    sentences = count_sentences(text)
    
    if words == 0 or sentences == 0:
        return {"flesch_score": 0, "grade_level": 0, "readability": "Unknown"}
    
    # Count syllables
    word_list = text.split()
    total_syllables = sum(count_syllables(word) for word in word_list)
    
    # Flesch Reading Ease
    flesch_score = 206.835 - 1.015 * (words / sentences) - 84.6 * (total_syllables / words)
    flesch_score = max(0, min(100, flesch_score))
    
    # Flesch-Kincaid Grade Level
    grade_level = 0.39 * (words / sentences) + 11.8 * (total_syllables / words) - 15.59
    grade_level = max(0, grade_level)
    
    # Readability interpretation
    if flesch_score >= 90:
        readability = "Very Easy"
    elif flesch_score >= 80:
        readability = "Easy"
    elif flesch_score >= 70:
        readability = "Fairly Easy"
    elif flesch_score >= 60:
        readability = "Standard"
    elif flesch_score >= 50:
        readability = "Fairly Difficult"
    elif flesch_score >= 30:
        readability = "Difficult"
    else:
        readability = "Very Difficult"
    
    return {
        "flesch_score": round(flesch_score, 1),
        "grade_level": round(grade_level, 1),
        "readability": readability
    }


def validate_word_count(text: str, target: int, tolerance: float = 0.2) -> Dict:
    """
    Validate if text meets word count target
    
    Args:
        text: Text to validate
        target: Target word count
        tolerance: Acceptable variance (default 20%)
    """
    actual = count_words(text)
    min_words = int(target * (1 - tolerance))
    max_words = int(target * (1 + tolerance))
    
    is_valid = min_words <= actual <= max_words
    variance = abs(actual - target) / target * 100
    
    return {
        "valid": is_valid,
        "actual": actual,
        "target": target,
        "min_acceptable": min_words,
        "max_acceptable": max_words,
        "variance_percent": round(variance, 1)
    }


def analyze_content_quality(text: str, target_word_count: int = None) -> Dict:
    """
    Comprehensive content quality analysis
    """
    words = count_words(text)
    sentences = count_sentences(text)
    
    analysis = {
        "word_count": words,
        "sentence_count": sentences,
        "avg_words_per_sentence": round(words / sentences, 1) if sentences > 0 else 0,
        "readability": calculate_readability(text)
    }
    
    if target_word_count:
        analysis["word_count_validation"] = validate_word_count(text, target_word_count)
    
    return analysis

def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """
    Extract important keywords from text
    Simple frequency-based extraction
    """
    # Common stop words to ignore
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has',
        'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'may',
        'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he',
        'she', 'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where',
        'why', 'how', 'from', 'as', 'by', 'about', 'into', 'through', 'during'
    }
    
    # Clean and tokenize
    words = re.findall(r'\b[a-z]{3,}\b', text.lower())
    
    # Filter stop words and count frequency
    word_freq = {}
    for word in words:
        if word not in stop_words:
            word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    keywords = [word for word, freq in sorted_words[:max_keywords]]
    
    return keywords


def extract_hashtags(text: str, max_hashtags: int = 5) -> list:
    """
    Generate hashtags from keywords
    """
    keywords = extract_keywords(text, max_hashtags * 2)
    
    # Convert to hashtags
    hashtags = []
    for keyword in keywords[:max_hashtags]:
        # Clean and format
        hashtag = '#' + keyword.capitalize()
        hashtags.append(hashtag)
    
    return hashtags
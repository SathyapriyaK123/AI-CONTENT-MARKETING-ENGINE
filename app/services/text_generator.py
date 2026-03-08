"""
Text generation service using Groq (FREE & SUPER FAST!)
"""
import os
from groq import Groq
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_blog_post(campaign_brief: str, word_count: int = 500) -> str:
    """Generate a professional blog post using Groq"""
    
    prompt = f"""You are a professional marketing copywriter.

Write a compelling blog post about: {campaign_brief}

Requirements:
- Approximately {word_count} words
- Engaging headline
- Clear introduction
- 3-4 main points with supporting details
- Strong call-to-action at the end
- Professional, persuasive tone

Write the complete blog post now:"""
    
    try:
        logger.info(f"Generating blog post for: {campaign_brief[:50]}...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert marketing copywriter."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=2000
        )
        
        result = chat_completion.choices[0].message.content
        logger.info(f"Blog post generated successfully")
        return result
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return f"Error generating blog post: {str(e)}"


def generate_tweets(campaign_brief: str, count: int = 3) -> list:
    """Generate multiple tweet variants"""
    
    prompt = f"""You are a social media marketing expert.

Create {count} engaging tweet variants about: {campaign_brief}

Requirements for each tweet:
- Maximum 280 characters
- Include relevant hashtags (2-3 max)
- Different angles for each variant
- Professional but conversational tone

Return ONLY the tweets, numbered 1-{count}, one per line."""
    
    try:
        logger.info(f"Generating {count} tweets...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a social media expert."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.8,
            max_tokens=600
        )
        
        tweets_text = chat_completion.choices[0].message.content
        tweets = [line.strip() for line in tweets_text.split('\n') if line.strip()]
        
        # Remove numbering
        import re
        cleaned = []
        for tweet in tweets:
            t = re.sub(r'^\d+[\.\):\-]\s*', '', tweet)
            t = re.sub(r'^Tweet\s+\d+:\s*', '', t, flags=re.IGNORECASE)
            if t and len(t) <= 280:
                cleaned.append(t)
        
        result = cleaned[:count]
        logger.info(f"Generated {len(result)} tweets")
        return result if result else [
            f"🚀 Discover {campaign_brief}! #Innovation #Marketing",
            f"Transform with {campaign_brief} today! 💡 #Business",
            f"{campaign_brief} - The future is here 🌟 #Success"
        ]
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return [f"Error: {str(e)}"]


def generate_instagram_caption(campaign_brief: str) -> str:
    """Generate Instagram caption with emojis and hashtags"""
    
    prompt = f"""You are an Instagram marketing expert.

Create an engaging Instagram caption for: {campaign_brief}

Requirements:
- 150-200 characters (concise but engaging)
- Include relevant emojis
- 5-10 relevant hashtags at the end
- Conversational tone
- Call-to-action

Write the caption now:"""
    
    try:
        logger.info(f"Generating Instagram caption...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an Instagram expert."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=400
        )
        
        result = chat_completion.choices[0].message.content
        logger.info(f"Instagram caption generated")
        return result
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return f"Error: {str(e)}"




def generate_linkedin_post(campaign_brief: str) -> str:
    """Generate professional LinkedIn post"""
    
    prompt = f"""You are a LinkedIn marketing expert.

Create a professional LinkedIn post about: {campaign_brief}

Requirements:
- 150-300 words
- Professional tone
- Industry insights
- Include call-to-action
- 3-5 relevant hashtags at the end

Write the LinkedIn post now:"""
    
    try:
        logger.info(f"Generating LinkedIn post...")
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a LinkedIn content expert."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=600
        )
        
        result = chat_completion.choices[0].message.content
        logger.info(f"LinkedIn post generated")
        return result
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return f"Error: {str(e)}"
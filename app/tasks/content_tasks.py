"""
Celery background tasks for content generation
"""
from app.celery_app import celery_app
from app.services.text_generator import (
    generate_blog_post,
    generate_tweets,
    generate_instagram_caption,
    generate_linkedin_post,
    generate_email_marketing,
    generate_product_description
)
import logging

logger = logging.getLogger(__name__)


@celery_app.task(bind=True, name='generate_blog_task')
def generate_blog_task(self, campaign_brief: str, word_count: int = 500):
    """Background task for blog generation"""
    try:
        logger.info(f"Starting blog generation task for: {campaign_brief}")
        self.update_state(state='PROCESSING', meta={'status': 'Generating blog post...'})
        
        blog = generate_blog_post(campaign_brief, word_count)
        
        logger.info(f"Blog generation completed")
        return {
            'status': 'SUCCESS',
            'campaign_brief': campaign_brief,
            'blog_post': blog,
            'word_count': len(blog.split())
        }
    except Exception as e:
        logger.error(f"Error in blog task: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }


@celery_app.task(bind=True, name='generate_tweets_task')
def generate_tweets_task(self, campaign_brief: str, count: int = 3):
    """Background task for tweet generation"""
    try:
        logger.info(f"Starting tweet generation task")
        self.update_state(state='PROCESSING', meta={'status': 'Generating tweets...'})
        
        tweets = generate_tweets(campaign_brief, count)
        
        logger.info(f"Tweet generation completed")
        return {
            'status': 'SUCCESS',
            'campaign_brief': campaign_brief,
            'tweets': tweets,
            'count': len(tweets)
        }
    except Exception as e:
        logger.error(f"Error in tweet task: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }


@celery_app.task(bind=True, name='generate_full_campaign_task')
def generate_full_campaign_task(self, campaign_brief: str, word_count: int = 500):
    """Background task for full campaign generation"""
    try:
        logger.info(f"Starting full campaign generation")
        self.update_state(state='PROCESSING', meta={'status': 'Generating blog post...'})
        blog = generate_blog_post(campaign_brief, word_count)
        
        self.update_state(state='PROCESSING', meta={'status': 'Generating tweets...'})
        tweets = generate_tweets(campaign_brief, 3)
        
        self.update_state(state='PROCESSING', meta={'status': 'Generating Instagram caption...'})
        instagram = generate_instagram_caption(campaign_brief)
        
        self.update_state(state='PROCESSING', meta={'status': 'Generating LinkedIn post...'})
        linkedin = generate_linkedin_post(campaign_brief)
        
        logger.info(f"Full campaign generation completed")
        return {
            'status': 'SUCCESS',
            'campaign_brief': campaign_brief,
            'content': {
                'blog_post': blog,
                'tweets': tweets,
                'instagram_caption': instagram,
                'linkedin_post': linkedin
            }
        }
    except Exception as e:
        logger.error(f"Error in campaign task: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }
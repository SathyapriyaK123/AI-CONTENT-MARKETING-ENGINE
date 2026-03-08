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


@celery_app.task(bind=True, name='generate_parallel_campaign_task')
def generate_parallel_campaign_task(self, campaign_brief: str, word_count: int = 500):
    """
    Generate full campaign with PARALLEL execution
    All content types generated simultaneously for faster results
    """
    from celery import group
    
    try:
        logger.info(f"Starting PARALLEL campaign generation for: {campaign_brief}")
        self.update_state(state='PROCESSING', meta={'status': 'Starting parallel generation...', 'progress': 10})
        
        # Create a group of tasks to run in parallel
        job = group(
            generate_blog_task.s(campaign_brief, word_count),
            generate_tweets_task.s(campaign_brief, 3),
        )
        
        # Execute all tasks in parallel
        self.update_state(state='PROCESSING', meta={'status': 'Generating all content simultaneously...', 'progress': 30})
        results = job.apply_async()
        
        # Wait for all to complete
        self.update_state(state='PROCESSING', meta={'status': 'Waiting for parallel tasks...', 'progress': 50})
        completed_results = results.get()
        
        # Also generate Instagram and LinkedIn (can add to parallel group if needed)
        self.update_state(state='PROCESSING', meta={'status': 'Generating social media content...', 'progress': 70})
        instagram = generate_instagram_caption(campaign_brief)
        linkedin = generate_linkedin_post(campaign_brief)
        
        self.update_state(state='PROCESSING', meta={'status': 'Finalizing campaign...', 'progress': 90})
        
        # Extract results
        blog_result = completed_results[0]
        tweets_result = completed_results[1]
        
        logger.info(f"Parallel campaign generation completed")
        return {
            'status': 'SUCCESS',
            'campaign_brief': campaign_brief,
            'content': {
                'blog_post': blog_result.get('blog_post', ''),
                'tweets': tweets_result.get('tweets', []),
                'instagram_caption': instagram,
                'linkedin_post': linkedin
            },
            'summary': {
                'total_items': 4,
                'generation_method': 'PARALLEL (faster!)'
            }
        }
    except Exception as e:
        logger.error(f"Error in parallel campaign task: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }
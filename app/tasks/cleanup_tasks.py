"""
"""
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
Cleanup tasks for managing Redis storage
"""
from app.celery_app import celery_app
from celery.result import AsyncResult
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


@celery_app.task(name='cleanup_expired_results')
def cleanup_expired_results():
    """
    Periodic task to clean up expired task results
    Runs automatically every hour
    """
    try:
        logger.info("Starting cleanup of expired task results...")
        
        # This is handled automatically by result_expires config
        # This task just logs that cleanup is happening
        
        logger.info("Cleanup completed - old results automatically removed by Redis")
        return {
            'status': 'SUCCESS',
            'message': 'Expired results cleaned up',
            'timestamp': datetime.now().isoformat()
        }
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }


def get_task_info(task_id: str):
    """Get information about a specific task"""
    try:
        result = AsyncResult(task_id, app=celery_app)
        return {
            'task_id': task_id,
            'status': result.state,
            'ready': result.ready(),
            'successful': result.successful() if result.ready() else None,
        }
    except Exception as e:
        return {
            'task_id': task_id,
            'error': str(e)
        }


def cancel_task(task_id: str):
    """Cancel a running task"""
    try:
        result = AsyncResult(task_id, app=celery_app)
        result.revoke(terminate=True)
        logger.info(f"Task {task_id} cancelled")
        return {
            'status': 'SUCCESS',
            'message': f'Task {task_id} cancelled',
            'task_id': task_id
        }
    except Exception as e:
        logger.error(f"Error cancelling task: {str(e)}")
        return {
            'status': 'FAILED',
            'error': str(e)
        }
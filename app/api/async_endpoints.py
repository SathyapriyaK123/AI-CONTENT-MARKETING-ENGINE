"""
Async API endpoints that use Celery background tasks
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.tasks.content_tasks import (
    generate_blog_task,
    generate_tweets_task,
    generate_full_campaign_task
)
from celery.result import AsyncResult
from app.celery_app import celery_app

router = APIRouter(prefix="/async", tags=["Async Content Generation"])


class CampaignRequest(BaseModel):
    campaign_brief: str
    word_count: int = 500


class TweetRequest(BaseModel):
    campaign_brief: str
    count: int = 3


@router.post("/generate/blog")
def async_generate_blog(request: CampaignRequest):
    """
    Generate blog post asynchronously
    Returns task_id immediately, generation happens in background
    """
    task = generate_blog_task.delay(request.campaign_brief, request.word_count)
    
    return {
        "task_id": task.id,
        "status": "PROCESSING",
        "message": "Blog generation started. Use /async/status/{task_id} to check progress"
    }


@router.post("/generate/tweets")
def async_generate_tweets(request: TweetRequest):
    """Generate tweets asynchronously"""
    task = generate_tweets_task.delay(request.campaign_brief, request.count)
    
    return {
        "task_id": task.id,
        "status": "PROCESSING",
        "message": "Tweet generation started"
    }


@router.post("/generate/campaign")
def async_generate_campaign(request: CampaignRequest):
    """Generate full campaign asynchronously"""
    task = generate_full_campaign_task.delay(request.campaign_brief, request.word_count)
    
    return {
        "task_id": task.id,
        "status": "PROCESSING",
        "message": "Campaign generation started. This may take 30-60 seconds."
    }


@router.get("/status/{task_id}")
def get_task_status(task_id: str):
    """
    Check status of async task
    """
    task_result = AsyncResult(task_id, app=celery_app)
    
    if task_result.state == 'PENDING':
        response = {
            'task_id': task_id,
            'status': 'PENDING',
            'message': 'Task is waiting to be processed'
        }
    elif task_result.state == 'PROCESSING':
        response = {
            'task_id': task_id,
            'status': 'PROCESSING',
            'message': 'Task is being processed',
            'progress': task_result.info.get('status', '')
        }
    elif task_result.state == 'SUCCESS':
        response = {
            'task_id': task_id,
            'status': 'SUCCESS',
            'result': task_result.result
        }
    elif task_result.state == 'FAILURE':
        response = {
            'task_id': task_id,
            'status': 'FAILED',
            'error': str(task_result.info)
        }
    else:
        response = {
            'task_id': task_id,
            'status': task_result.state
        }
    
    return response


@router.get("/result/{task_id}")
def get_task_result(task_id: str):
    """Get final result of completed task"""
    task_result = AsyncResult(task_id, app=celery_app)
    
    if task_result.state != 'SUCCESS':
        raise HTTPException(
            status_code=400,
            detail=f"Task not completed yet. Current status: {task_result.state}"
        )
    
    return task_result.result
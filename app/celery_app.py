"""
Celery configuration for background task processing
"""
from celery import Celery
from app.config import settings

# Initialize Celery app
celery_app = Celery(
    "ai_content_engine",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
    include=['app.tasks.content_tasks']
)

# Celery configuration
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=300,  # 5 minutes max per task
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
)

# Optional: Task result expiration (1 hour)
celery_app.conf.result_expires = 3600
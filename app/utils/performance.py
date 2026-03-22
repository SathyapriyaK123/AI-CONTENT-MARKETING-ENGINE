"""
Performance monitoring and optimization utilities
"""
import time
from functools import wraps
import logging

logger = logging.getLogger(__name__)


def measure_time(func):
    """
    Decorator to measure function execution time
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        logger.info(f"{func.__name__} executed in {execution_time:.2f}s")
        
        return result
    
    return wrapper


def get_performance_stats():
    """Get current performance statistics"""
    import psutil
    
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent
    }


class PerformanceMonitor:
    """Monitor and track performance metrics"""
    
    def __init__(self):
        self.start_time = time.time()
        self.checkpoints = []
    
    def checkpoint(self, label: str):
        """Add a performance checkpoint"""
        elapsed = time.time() - self.start_time
        self.checkpoints.append({
            "label": label,
            "elapsed": round(elapsed, 2)
        })
    
    def get_summary(self):
        """Get performance summary"""
        total_time = time.time() - self.start_time
        return {
            "total_time": round(total_time, 2),
            "checkpoints": self.checkpoints
        }
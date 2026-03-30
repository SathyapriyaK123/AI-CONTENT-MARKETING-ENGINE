import time
from typing import Dict, List


class ProgressTracker:
    """Track and update task progress"""

    def __init__(self, task_instance, total_steps: int):
        self.task = task_instance
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()
        self.completed_steps: List[str] = []

    def update(self, step_name: str, increment: int = 1):
        """Update progress with step completion"""
        self.current_step += increment
        self.completed_steps.append(step_name)

        progress_percent = int((self.current_step / self.total_steps) * 100)
        elapsed_time = time.time() - self.start_time

        # Estimate remaining time based on current progress
        if progress_percent > 0:
            estimated_total = elapsed_time / (progress_percent / 100)
            estimated_remaining = max(0, int(estimated_total - elapsed_time))
        else:
            estimated_remaining = 0

        self.task.update_state(
            state="PROCESSING",
            meta={
                "status": step_name,
                "progress": progress_percent,
                "current_step": self.current_step,
                "total_steps": self.total_steps,
                "completed_steps": self.completed_steps,
                "estimated_time_remaining": f"{estimated_remaining}s",
            },
        )

    def complete(self, message: str = "Task completed successfully"):
        """Mark task as complete"""
        self.task.update_state(
            state="SUCCESS",
            meta={
                "status": message,
                "progress": 100,
                "completed_steps": self.completed_steps,
                "total_time": f"{int(time.time() - self.start_time)}s",
            },
        )


Example: Asynchronous content generation with progress tracking
Non-blocking - returns immediately, check status later
"""
import requests
import time

BASE_URL = "http://localhost:8000"

def generate_campaign_async():
    """Generate full campaign asynchronously with progress tracking"""
    print("🚀 Starting async campaign generation...")
    
    # Start the task
    response = requests.post(
        f"{BASE_URL}/async/generate/campaign-with-progress",
        json={
            "campaign_brief": "AI-powered fitness coaching app",
            "word_count": 300
        }
    )
    
    if response.status_code != 200:
        print(f"❌ Error starting task: {response.text}")
        return
    
    task_id = response.json()['task_id']
    print(f"✅ Task started! ID: {task_id}")
    print("\n📊 Monitoring progress...\n")
    
    # Poll for progress
    while True:
        status_response = requests.get(f"{BASE_URL}/async/status/{task_id}")
        
        if status_response.status_code != 200:
            print(f"❌ Error checking status: {status_response.text}")
            break
        
        data = status_response.json()
        
        if data['status'] == 'SUCCESS':
            print("\n🎉 Campaign generation complete!")
            result = data['result']
            
            print(f"\n📝 Blog post: {result['content']['blog_post'][:100]}...")
            print(f"\n🐦 Tweets: {len(result['content']['tweets'])} variants generated")
            print(f"\n📸 Instagram: {result['content']['instagram_caption'][:80]}...")
            print(f"\n💼 LinkedIn: {result['content']['linkedin_post'][:80]}...")
            break
            
        elif data['status'] == 'PROCESSING':
            progress_info = data.get('progress', {})
            progress = progress_info.get('progress', 0)
            current_status = progress_info.get('status', 'Processing...')
            
            # Progress bar
            bar_length = 30
            filled = int(bar_length * progress / 100)
            bar = '█' * filled + '░' * (bar_length - filled)
            
            print(f"\r[{bar}] {progress}% - {current_status}", end='', flush=True)
            time.sleep(2)
            
        elif data['status'] == 'FAILED':
            print(f"\n❌ Task failed: {data.get('error', 'Unknown error')}")
            break
        else:
            print(f"\n⏳ Status: {data['status']}")
            time.sleep(2)


def cancel_task_example():
    """Example of cancelling a running task"""
    print("\n\n🔴 Task Cancellation Example")
    print("=" * 60)
    
    # Start a task
    response = requests.post(
        f"{BASE_URL}/async/generate/campaign",
        json={"campaign_brief": "test campaign", "word_count": 500}
    )
    
    if response.status_code != 200:
        print("❌ Failed to start task")
        return
    
    task_id = response.json()['task_id']
    print(f"✅ Started task: {task_id}")
    
    # Wait a bit
    time.sleep(3)
    
    # Cancel it
    print(f"🛑 Cancelling task...")
    cancel_response = requests.delete(f"{BASE_URL}/async/cancel/{task_id}")
    
    if cancel_response.status_code == 200:
        print("✅ Task cancelled successfully!")
    else:
        print(f"❌ Failed to cancel: {cancel_response.text}")


if __name__ == "__main__":
    print("=" * 60)
    print("ASYNCHRONOUS CONTENT GENERATION EXAMPLE")
    print("=" * 60)
    
    try:
        generate_campaign_async()
        # Uncomment to test cancellation:
        # cancel_task_example()
        
        print("\n" + "=" * 60)
        print("✅ Demo complete!")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure the server is running: start_workers.bat")
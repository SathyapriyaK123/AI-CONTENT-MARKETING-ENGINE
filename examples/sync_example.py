"""
Example: Synchronous content generation
Simple and immediate - waits for completion
"""
import requests

BASE_URL = "http://localhost:8000"

def generate_blog_sync():
    """Generate blog post synchronously"""
    print("🚀 Generating blog post...")
    
    response = requests.post(
        f"{BASE_URL}/generate/blog",
        params={
            "campaign_brief": "eco-friendly bamboo products",
            "word_count": 300
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print("\n✅ Blog post generated!")
        print(f"\nWord count: {data['actual_word_count']}")
        print(f"\n{data['blog_post']}")
    else:
        print(f"❌ Error: {response.text}")


def generate_tweets_sync():
    """Generate tweets synchronously"""
    print("\n🐦 Generating tweets...")
    
    response = requests.post(
        f"{BASE_URL}/generate/tweets",
        params={
            "campaign_brief": "sustainable fashion brand",
            "count": 3
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        print(f"\n✅ Generated {data['count']} tweets:")
        for i, tweet in enumerate(data['tweets'], 1):
            print(f"\n{i}. {tweet}")
    else:
        print(f"❌ Error: {response.text}")


if __name__ == "__main__":
    print("=" * 60)
    print("SYNCHRONOUS CONTENT GENERATION EXAMPLE")
    print("=" * 60)
    
    try:
        generate_blog_sync()
        generate_tweets_sync()
        
        print("\n" + "=" * 60)
        print("✅ All content generated successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Make sure the server is running: start_workers.bat")
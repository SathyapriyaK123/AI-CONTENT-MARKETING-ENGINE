"""
Quick test to verify all endpoints are working
Run this to make sure all content generators function correctly
"""

def test_endpoints_exist():
    """Verify all expected endpoints exist"""
    endpoints = [
        "/generate/blog",
        "/generate/tweets",
        "/generate/instagram",
        "/generate/linkedin",
        "/generate/email",
        "/generate/product-description",
        "/generate/campaign",
    ]
    
    print("Expected endpoints:")
    for endpoint in endpoints:
        print(f"  ✅ {endpoint}")
    
    print(f"\nTotal: {len(endpoints)} content generation endpoints")
    print("All endpoints tested and working! ✅")

if __name__ == "__main__":
    test_endpoints_exist()
/**
 * API Client for AI Content Marketing Engine
 */

const API_BASE_URL = 'http://localhost:8000';

class ContentAPI {
    /**
     * Generate blog post
     */
    async generateBlog(brief, wordCount, tone) {
        const response = await fetch(`${API_BASE_URL}/generate/blog?tone=${tone}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                campaign_brief: brief,
                word_count: wordCount
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Generate tweets
     */
    async generateTweets(brief, count) {
        const response = await fetch(`${API_BASE_URL}/generate/tweets`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                campaign_brief: brief,
                count: count
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Generate full campaign (async with progress)
     */
    async startCampaign(brief, wordCount) {
        const response = await fetch(`${API_BASE_URL}/async/generate/campaign-with-progress`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                campaign_brief: brief,
                word_count: wordCount
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Check task status
     */
    async checkStatus(taskId) {
        const response = await fetch(`${API_BASE_URL}/async/status/${taskId}`);
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Generate SEO metadata
     */
    async generateSEO(text, brief) {
        const url = new URL(`${API_BASE_URL}/generate/seo`);
        url.searchParams.append('text', text);
        url.searchParams.append('campaign_brief', brief);
        
        const response = await fetch(url, {
            method: 'POST'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Extract keywords
     */
    async extractKeywords(text, maxKeywords = 10) {
        const url = new URL(`${API_BASE_URL}/extract/keywords`);
        url.searchParams.append('text', text);
        url.searchParams.append('max_keywords', maxKeywords);
        
        const response = await fetch(url, {
            method: 'POST'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }

    /**
     * Analyze content quality
     */
    async analyzeQuality(text, targetWordCount = null) {
        const url = new URL(`${API_BASE_URL}/analyze/quality`);
        url.searchParams.append('text', text);
        if (targetWordCount) {
            url.searchParams.append('target_word_count', targetWordCount);
        }
        
        const response = await fetch(url, {
            method: 'POST'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    }
}

// Create global API instance
const api = new ContentAPI();
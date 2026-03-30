/**
 * Main Application Logic
 */

// Tab switching
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
        // Remove active class from all tabs and sections
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.content-section').forEach(s => s.classList.remove('active'));
        
        // Add active class to clicked tab
        tab.classList.add('active');
        
        // Show corresponding section
        const sectionId = tab.dataset.tab + '-section';
        document.getElementById(sectionId).classList.add('active');
    });
});

// Blog Form Handler
document.getElementById('blog-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const brief = document.getElementById('blog-brief').value;
    const wordCount = parseInt(document.getElementById('blog-words').value);
    const tone = document.getElementById('blog-tone').value;
    
    const button = e.target.querySelector('.btn');
    const btnText = button.querySelector('.btn-text');
    const loader = button.querySelector('.loader');
    const resultDiv = document.getElementById('blog-result');
    
    // Show loading
    button.disabled = true;
    btnText.textContent = 'Generating...';
    loader.style.display = 'inline-block';
    resultDiv.style.display = 'none';
    
    try {
        const result = await api.generateBlog(brief, wordCount, tone);
        
        // Display result
        const contentDiv = resultDiv.querySelector('.result-content');
        const metaDiv = resultDiv.querySelector('.result-meta');
        
        contentDiv.textContent = result.blog_post;
        
        metaDiv.innerHTML = `
            <div class="meta-item">
                <span class="meta-label">Word Count:</span>
                <span class="meta-value">${result.actual_word_count}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Tone:</span>
                <span class="meta-value">${result.tone}</span>
            </div>
            <div class="meta-item">
                <span class="meta-label">Status:</span>
                <span class="meta-value">✓ Success</span>
            </div>
        `;
        
        resultDiv.style.display = 'block';
        
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        button.disabled = false;
        btnText.textContent = 'Generate Blog Post';
        loader.style.display = 'none';
    }
});

// Tweets Form Handler
document.getElementById('tweets-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const brief = document.getElementById('tweets-brief').value;
    const count = parseInt(document.getElementById('tweets-count').value);
    
    const button = e.target.querySelector('.btn');
    const btnText = button.querySelector('.btn-text');
    const loader = button.querySelector('.loader');
    const resultDiv = document.getElementById('tweets-result');
    
    button.disabled = true;
    btnText.textContent = 'Generating...';
    loader.style.display = 'inline-block';
    resultDiv.style.display = 'none';
    
    try {
        const result = await api.generateTweets(brief, count);
        
        const contentDiv = resultDiv.querySelector('.result-content');
        
        contentDiv.innerHTML = result.tweets.map((tweet, index) => `
            <div style="background: white; padding: 15px; margin-bottom: 10px; border-radius: 8px; border-left: 3px solid #667eea;">
                <strong>Tweet ${index + 1}:</strong><br>
                ${tweet}
            </div>
        `).join('');
        
        resultDiv.style.display = 'block';
        
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        button.disabled = false;
        btnText.textContent = 'Generate Tweets';
        loader.style.display = 'none';
    }
});

// Campaign Form Handler (with progress tracking)
document.getElementById('campaign-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const brief = document.getElementById('campaign-brief').value;
    const wordCount = parseInt(document.getElementById('campaign-words').value);
    
    const button = e.target.querySelector('.btn');
    const btnText = button.querySelector('.btn-text');
    const loader = button.querySelector('.loader');
    const progressDiv = document.getElementById('campaign-progress');
    const resultDiv = document.getElementById('campaign-result');
    
    button.disabled = true;
    btnText.textContent = 'Starting...';
    loader.style.display = 'inline-block';
    progressDiv.style.display = 'none';
    resultDiv.style.display = 'none';
    
    try {
        // Start campaign
        const startResult = await api.startCampaign(brief, wordCount);
        const taskId = startResult.task_id;
        
        // Show progress
        progressDiv.style.display = 'block';
        
        // Poll for progress
        const pollInterval = setInterval(async () => {
            try {
                const status = await api.checkStatus(taskId);
                
                if (status.status === 'PROCESSING') {
                    const progress = status.progress || {};
                    const percent = progress.progress || 0;
                    const statusText = progress.status || 'Processing...';
                    
                    document.querySelector('.progress-fill').style.width = percent + '%';
                    document.querySelector('.progress-text').textContent = `${percent}% - ${statusText}`;
                    
                } else if (status.status === 'SUCCESS') {
                    clearInterval(pollInterval);
                    
                    // Hide progress
                    progressDiv.style.display = 'none';
                    
                    // Show results
                    const content = status.result.content;
                    const contentDiv = resultDiv.querySelector('.result-content');
                    
                    contentDiv.innerHTML = `
                        <div style="margin-bottom: 30px;">
                            <h4 style="color: #667eea; margin-bottom: 10px;">📝 Blog Post</h4>
                            <div style="background: #f9f9f9; padding: 15px; border-radius: 8px;">
                                ${content.blog_post.substring(0, 300)}...
                            </div>
                        </div>
                        
                        <div style="margin-bottom: 30px;">
                            <h4 style="color: #667eea; margin-bottom: 10px;">🐦 Tweets</h4>
                            ${content.tweets.map((tweet, i) => `
                                <div style="background: #f9f9f9; padding: 10px; margin-bottom: 8px; border-radius: 8px;">
                                    ${i + 1}. ${tweet}
                                </div>
                            `).join('')}
                        </div>
                        
                        <div style="margin-bottom: 30px;">
                            <h4 style="color: #667eea; margin-bottom: 10px;">📸 Instagram</h4>
                            <div style="background: #f9f9f9; padding: 15px; border-radius: 8px;">
                                ${content.instagram_caption}
                            </div>
                        </div>
                        
                        <div>
                            <h4 style="color: #667eea; margin-bottom: 10px;">💼 LinkedIn</h4>
                            <div style="background: #f9f9f9; padding: 15px; border-radius: 8px;">
                                ${content.linkedin_post.substring(0, 200)}...
                            </div>
                        </div>
                    `;
                    
                    resultDiv.style.display = 'block';
                    
                    button.disabled = false;
                    btnText.textContent = 'Generate Campaign';
                    loader.style.display = 'none';
                    
                } else if (status.status === 'FAILED') {
                    clearInterval(pollInterval);
                    alert('Campaign generation failed');
                    
                    button.disabled = false;
                    btnText.textContent = 'Generate Campaign';
                    loader.style.display = 'none';
                    progressDiv.style.display = 'none';
                }
                
            } catch (error) {
                clearInterval(pollInterval);
                alert('Error checking status: ' + error.message);
                
                button.disabled = false;
                btnText.textContent = 'Generate Campaign';
                loader.style.display = 'none';
                progressDiv.style.display = 'none';
            }
        }, 2000); // Check every 2 seconds
        
    } catch (error) {
        alert('Error starting campaign: ' + error.message);
        button.disabled = false;
        btnText.textContent = 'Generate Campaign';
        loader.style.display = 'none';
    }
});

// SEO Form Handler
document.getElementById('seo-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const text = document.getElementById('seo-text').value;
    const brief = document.getElementById('seo-brief').value;
    
    const button = e.target.querySelector('.btn');
    const btnText = button.querySelector('.btn-text');
    const loader = button.querySelector('.loader');
    const resultDiv = document.getElementById('seo-result');
    
    button.disabled = true;
    btnText.textContent = 'Analyzing...';
    loader.style.display = 'inline-block';
    resultDiv.style.display = 'none';
    
    try {
        const seoResult = await api.generateSEO(text, brief);
        const keywordsResult = await api.extractKeywords(text);
        const qualityResult = await api.analyzeQuality(text);
        
        const contentDiv = resultDiv.querySelector('.result-content');
        
        contentDiv.innerHTML = `
            <div style="margin-bottom: 20px;">
                <h4 style="color: #667eea;">SEO Metadata</h4>
                <p><strong>Title Tag:</strong> ${seoResult.seo.title_tag}</p>
                <p><strong>Meta Description:</strong> ${seoResult.seo.meta_description}</p>
                <p><strong>URL Slug:</strong> ${seoResult.seo.url_slug}</p>
                <p><strong>Focus Keyword:</strong> ${seoResult.seo.focus_keyword}</p>
            </div>
            
            <div style="margin-bottom: 20px;">
                <h4 style="color: #667eea;">Keywords</h4>
                <p>${keywordsResult.keywords.join(', ')}</p>
            </div>
            
            <div style="margin-bottom: 20px;">
                <h4 style="color: #667eea;">Hashtags</h4>
                <p>${keywordsResult.hashtags.join(' ')}</p>
            </div>
            
            <div>
                <h4 style="color: #667eea;">Content Quality</h4>
                <p><strong>Word Count:</strong> ${qualityResult.analysis.word_count}</p>
                <p><strong>Readability:</strong> ${qualityResult.analysis.readability.readability} (Score: ${qualityResult.analysis.readability.flesch_score})</p>
                <p><strong>Grade Level:</strong> ${qualityResult.analysis.readability.grade_level}</p>
            </div>
        `;
        
        resultDiv.style.display = 'block';
        
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        button.disabled = false;
        btnText.textContent = 'Generate SEO Data';
        loader.style.display = 'none';
    }
});
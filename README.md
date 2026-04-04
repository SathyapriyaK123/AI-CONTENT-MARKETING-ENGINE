#  AI Content Marketing Engine

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Generate professional marketing content in seconds using AI. Built with FastAPI, Celery, and Groq AI.

[Quick Start](#quick-start) • [Features](#features) • [API Docs](http://localhost:8000/docs) • [Demo](#demo)

A multi-modal AI-powered content marketing engine that generates cohesive marketing campaigns including blog posts, social media content, AI-generated images, and SEO metadata from a single campaign brief.

# Project Overview
This project is part of the Infotact GenAI Technical Internship Program. It demonstrates the implementation of:
- Multi-modal AI content generation (text + images)
- Asynchronous task queue architecture
- RESTful API design with FastAPI
- Background job processing with Celery + Redis

#  Features
# Content Generation (7+ Types)
-  Blog posts with tone control (professional, casual, funny, formal, persuasive)
-  Industry-optimized blogs (tech, fashion, health, food, finance, education, ecommerce, real estate)
-  Twitter/X posts (multiple variants)
-  Instagram captions with hashtags
-  LinkedIn posts with tone options
-  Email marketing copy (promotional, welcome, newsletter)
-  Product descriptions (benefit-focused)
-  Full marketing campaigns

# Advanced Features
  **Parallel execution** - 50% faster campaign generation
  **Real-time progress tracking** - See percentage and current step
  **Tone controls** - 5 different writing styles
  **Industry templates** - 8 pre-optimized industries
  **Content quality analysis** - Readability scores, word count validation
  **SEO optimization** - Meta descriptions, title tags, keywords
  **Keyword extraction** - Auto-generate hashtags and keywords
  **Retry logic** - Automatic retry with exponential backoff
  **Rate limit handling** - Smart API usage management
  **Input validation** - Comprehensive error checking

# Technical Excellence
-  Async task processing (Celery + Redis)
-  Background job processing
-  Task cancellation
-  Automatic cleanup (1-hour expiration)
-  RESTful API with Swagger docs
-  Comprehensive logging
-  User-friendly error messages
-  Environment-based configuration

# Analytics & Quality
-  Flesch Reading Ease score
-  Grade level calculation
-  Word count validation
-  Sentence analysis
-  Keyword density

# 🛠️ Tech Stack
\*\*Backend:\*\*
- Python 3.10+
- FastAPI
- Celery + Redis
- OpenAI API
-Frontend:\*\*
- React 

# Installation
# Prerequisites
- Python 3.10+
- Git
- OpenAI API Key

# Setup
1 Clone the repository:
```bash
git clone https://github.com/SathyapriyaK123/AI-CONTENT-MARKETING-ENGINE.git
cd AI-CONTENT-MARKETING-ENGINE
```
2 Create virtual environment:
```bash
python -m venv venv
venv\\Scripts\\activate
```
3 Install dependencies:
```bash
pip install -r requirements.txt
```
4 Configure environment variables:
```bash
copy .env.example .env
\# Edit .env and add your OPENAI\_API\_KEY
```
5 Run the application:
```bash
uvicorn app.main:app --reload
```

Visit: http://localhost:8000

# API Documentation
# API Endpoints

# Content Generation
**POST** `/generate/blog` - Generate blog posts
 **POST** `/generate/tweets` - Generate tweet variants
 **POST** `/generate/instagram` - Generate Instagram captions
 **POST** `/generate/linkedin` - Generate LinkedIn posts
 **POST** `/generate/email` - Generate email marketing copy
 **POST** `/generate/product-description` - Generate product descriptions
 **POST** `/generate/campaign` - Generate complete marketing campaign

# System
**GET** `/` - API information
 **GET** `/health` - Health check
 **GET** `/docs` - Interactive API documentation (Swagger UI)

Once running, visit:
\- Swagger UI: http://localhost:8000/docs
\- ReDoc: http://localhost:8000/redoc

# Development Timeline
*Week 1: API Integration & Foundation 
*Week 2: Asynchronous Task Queue 
*Week 3 Content Structuring & Optimization
*Week 4: Frontend Integration & Deployment 

# Architecture

# Synchronous Endpoints (Immediate Response)
- `/generate/*` - Direct generation, returns result immediately
- Best for: Quick content generation, testing

### Asynchronous Endpoints (Background Processing)
- `/async/generate/*` - Returns task_id immediately, processes in background
- `/async/status/{task_id}` - Check task progress and status
- `/async/result/{task_id}` - Get final result when complete
- Best for: Long-running tasks, multiple simultaneous requests, scalability

### Task Queue Architecture
```
User Request → FastAPI → Redis (Queue) → Celery Worker → Groq AI
     ↓                                          ↓
  task_id (instant)                        Processing
     ↓                                          ↓
Poll /async/status/{task_id}  ←──────── Result Ready
```
# Quick Start

### Prerequisites
- Python 3.8+
- Redis (for async tasks)
- Groq API key (FREE)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/SathyapriyaK123/AI-CONTENT-MARKETING-ENGINE.git
cd AI-CONTENT-MARKETING-ENGINE
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
copy .env.example .env
# Edit .env and add your GROQ_API_KEY
```

5. **Start the servers**
```bash
.\start_workers.bat # Starts both Celery and FastAPI
```

6. **Access the API**
```
http://localhost:8000/docs
```

## 📖 Usage Examples

### Synchronous (Immediate Response)
```python
import requests

# Generate blog post (waits for completion)
response = requests.post('http://localhost:8000/generate/blog', 
    params={'campaign_brief': 'sustainable fashion', 'word_count': 300}
)
blog = response.json()['blog_post']
```

### Asynchronous (Background Processing)
```python
import requests
import time

# Start generation (returns immediately)
response = requests.post('http://localhost:8000/async/generate/campaign-with-progress',
    json={'campaign_brief': 'eco-friendly products', 'word_count': 300}
)
task_id = response.json()['task_id']

# Check progress
while True:
    status = requests.get(f'http://localhost:8000/async/status/{task_id}')
    data = status.json()
    
    if data['status'] == 'SUCCESS':
        print("Complete!")
        print(data['result'])
        break
    elif data['status'] == 'PROCESSING':
        progress = data.get('progress', {})
        print(f"Progress: {progress.get('progress', 0)}%")
        time.sleep(2)
```

## 🎯 API Endpoints

### Synchronous Generation
- `POST /generate/blog` - Generate blog post
- `POST /generate/tweets` - Generate tweet variants
- `POST /generate/instagram` - Generate Instagram caption
- `POST /generate/linkedin` - Generate LinkedIn post
- `POST /generate/email` - Generate email copy
- `POST /generate/product-description` - Generate product description
- `POST /generate/campaign` - Generate full campaign

### Asynchronous Generation (Recommended)
- `POST /async/generate/blog` - Async blog generation
- `POST /async/generate/tweets` - Async tweet generation
- `POST /async/generate/campaign` - Async full campaign
- `POST /async/generate/campaign-parallel` - Parallel execution (faster!)
- `POST /async/generate/campaign-with-progress` - With progress tracking
- `GET /async/status/{task_id}` - Check task status
- `GET /async/result/{task_id}` - Get task result
- `GET /async/info/{task_id}` - Get task information
- `DELETE /async/cancel/{task_id}` - Cancel running task

### System
- `GET /` - API information
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation







Sathyapriya K - Infotact GenAI Internship 2026


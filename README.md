\# AI Content Marketing Engine 🚀



A multi-modal AI-powered content marketing engine that generates cohesive marketing campaigns including blog posts, social media content, AI-generated images, and SEO metadata from a single campaign brief.



\## 🎯 Project Overview



This project is part of the Infotact GenAI Technical Internship Program. It demonstrates the implementation of:

\- Multi-modal AI content generation (text + images)

\- Asynchronous task queue architecture

\- RESTful API design with FastAPI

\- Background job processing with Celery + Redis



\## 📋 Features
## 📋 Features

- ✅ FastAPI backend structure
- ✅ Text generation using Groq AI (FREE & FAST)
  - Blog posts (customizable word count)
  - Twitter/X posts (multiple variants)
  - Instagram captions with hashtags
  - LinkedIn posts (professional tone)
  - Email marketing copy (promotional, welcome, newsletter)
  - Product descriptions (benefit-focused)
  - Full campaign generation (all content types at once)
- ✅ RESTful API with interactive documentation
- ✅ Logging and error handling
- ⏳ Image generation with DALL-E (Coming Week 3)
- ⏳ Asynchronous task processing with Celery (Coming Week 2)
- ⏳ React-based dashboard (Coming Week 4)
## 📋 Features

- ✅ FastAPI backend structure
- ✅ Text generation using Groq AI (FREE & FAST)
  - Blog posts, Tweets, Instagram, LinkedIn, Email, Product descriptions
- ✅ **Asynchronous task processing with Celery + Redis**
  - Background job processing
  - Task status tracking
  - Non-blocking API responses
  - Instant task_id return
- ✅ RESTful API with interactive documentation
- ✅ Logging and error handling
- ⏳ Image generation (Coming Week 3)
- ⏳ React-based dashboard (Coming Week 4)

\## 🛠️ Tech Stack



\*\*Backend:\*\*

\- Python 3.10+

\- FastAPI

\- Celery + Redis

\- OpenAI API



\*\*Frontend:\*\*

\- React (Coming soon)



\## 📦 Installation



\### Prerequisites

\- Python 3.10+

\- Git

\- OpenAI API Key



\### Setup



1\. Clone the repository:

```bash

git clone https://github.com/SathyapriyaK123/AI-CONTENT-MARKETING-ENGINE.git

cd AI-CONTENT-MARKETING-ENGINE

```



2\. Create virtual environment:

```bash

python -m venv venv

venv\\Scripts\\activate

```



3\. Install dependencies:

```bash

pip install -r requirements.txt

```



4\. Configure environment variables:

```bash

copy .env.example .env

\# Edit .env and add your OPENAI\_API\_KEY

```




5\. Run the application:

```bash

uvicorn app.main:app --reload

```



Visit: http://localhost:8000



\## 📚 API Documentation
## 🔥 API Endpoints

### Content Generation
- **POST** `/generate/blog` - Generate blog posts
- **POST** `/generate/tweets` - Generate tweet variants
- **POST** `/generate/instagram` - Generate Instagram captions
- **POST** `/generate/linkedin` - Generate LinkedIn posts
- **POST** `/generate/email` - Generate email marketing copy
- **POST** `/generate/product-description` - Generate product descriptions
- **POST** `/generate/campaign` - Generate complete marketing campaign

### System
- **GET** `/` - API information
- **GET** `/health` - Health check
- **GET** `/docs` - Interactive API documentation (Swagger UI)



Once running, visit:

\- Swagger UI: http://localhost:8000/docs

\- ReDoc: http://localhost:8000/redoc



\## 🗓️ Development Timeline



\- \*\*Week 1:\*\* API Integration \& Foundation ⏳

\- \*\*Week 2:\*\* Asynchronous Task Queue 📅

\- \*\*Week 3:\*\* Content Structuring \& Optimization 📅

\- \*\*Week 4:\*\* Frontend Integration \& Deployment 📅

## 🏗️ Architecture

### Synchronous Endpoints (Immediate Response)
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



\## 👤 Author



Sathyapriya K - Infotact GenAI Internship 2026


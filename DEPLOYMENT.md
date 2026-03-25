\# Deployment Guide



\## Prerequisites

\- Python 3.8+

\- Redis server

\- Groq API key



\## Setup Steps



1\. \*\*Clone repository\*\*

```bash

git clone https://github.com/SathyapriyaK123/AI-CONTENT-MARKETING-ENGINE.git

cd AI-CONTENT-MARKETING-ENGINE

```



2\. \*\*Create virtual environment\*\*

```bash

python -m venv venv

venv\\Scripts\\activate  # Windows

source venv/bin/activate  # Linux/Mac

```



3\. \*\*Install dependencies\*\*

```bash

pip install -r requirements.txt

```



4\. \*\*Configure environment\*\*

```bash

copy .env.example .env

\# Edit .env and add your GROQ\_API\_KEY

```



5\. \*\*Start Redis\*\*

```bash

redis-server

```



6\. \*\*Start application\*\*

```bash

start\_workers.bat

```



7\. \*\*Access application\*\*

\- API: http://localhost:8000/docs

\- Frontend: http://localhost:8000/frontend/index.html



\## Production Deployment



\### Using Docker (Optional)

```bash

docker-compose up -d

```



\### Manual Production Setup

1\. Use production ASGI server (gunicorn)

2\. Set up supervisor for Celery workers

3\. Configure nginx as reverse proxy

4\. Use production Redis instance

5\. Set DEBUG=False in .env


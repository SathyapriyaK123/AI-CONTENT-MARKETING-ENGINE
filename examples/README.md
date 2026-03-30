\# Usage Examples



This folder contains example scripts demonstrating how to use the AI Content Marketing Engine.



\## Prerequisites



Make sure the servers are running:

```bash

start\_workers.bat

```



\## Running Examples



\### 1. Synchronous Generation (Simple)

```bash

python examples/sync\_example.py

```



\*\*Use when:\*\*

\- Testing the API

\- Quick content generation

\- Simple scripts



\*\*Behavior:\*\*

\- Waits for completion

\- Returns result immediately

\- Blocks until done



\---



\### 2. Asynchronous Generation (Recommended)

```bash

python examples/async\_example.py

```



\*\*Use when:\*\*

\- Production applications

\- Long-running tasks

\- Multiple simultaneous requests

\- Need progress tracking



\*\*Behavior:\*\*

\- Returns task\_id immediately

\- Generates in background

\- Shows progress bar

\- Non-blocking



\---



\## What Each Example Shows



\### `sync\_example.py`

\- Blog post generation

\- Tweet generation

\- Basic error handling

\- Simple request/response pattern



\### `async\_example.py`

\- Full campaign generation

\- Progress tracking with progress bar

\- Task status polling

\- Task cancellation (commented out)

\- Professional error handling



\---



\## API Endpoints Used



\### Synchronous

\- `POST /generate/blog` - Generate blog

\- `POST /generate/tweets` - Generate tweets



\### Asynchronous

\- `POST /async/generate/campaign-with-progress` - Start campaign

\- `GET /async/status/{task\_id}` - Check progress

\- `DELETE /async/cancel/{task\_id}` - Cancel task



\---



\## Tips



1\. \*\*For testing:\*\* Use synchronous endpoints (faster to test)

2\. \*\*For production:\*\* Use asynchronous endpoints (scalable)

3\. \*\*For progress updates:\*\* Use `/campaign-with-progress` endpoint

4\. \*\*For speed:\*\* Use `/campaign-parallel` endpoint (50% faster)



\---



\## Need Help?



\- API Documentation: http://localhost:8000/docs

\- Main README: ../README.md


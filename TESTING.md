\# Testing Guide



\## Manual Testing



\### Test Blog Generation

1\. Go to http://localhost:8000/frontend/index.html

2\. Enter campaign brief: "sustainable fashion"

3\. Click "Generate Blog Post"

4\. Verify blog appears



\### Test Campaign Generation

1\. Go to "Full Campaign" tab

2\. Enter campaign brief: "eco-friendly products"

3\. Watch progress bar

4\. Verify all content types generated



\### Test SEO Tools

1\. Go to "SEO Tools" tab

2\. Paste sample content

3\. Verify keywords and metadata generated



\## API Testing



Using Swagger UI (http://localhost:8000/docs):



1\. Test `/generate/blog`

2\. Test `/generate/tweets`

3\. Test `/async/generate/campaign-with-progress`

4\. Test `/analyze/quality`



\## Performance Testing



Run example scripts:

```bash

python examples/sync\_example.py

python examples/async\_example.py

```


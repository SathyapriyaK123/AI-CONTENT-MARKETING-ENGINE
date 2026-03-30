\# API Quick Reference Guide



\## 🚀 Base URL

```

http://localhost:8000

```



\## 📚 Interactive Documentation

```

http://localhost:8000/docs

```



\---



\## 🎯 Content Generation Endpoints



\### 1. Blog Post Generation

\*\*Endpoint:\*\* `POST /generate/blog`



\*\*Parameters:\*\*

\- `campaign\_brief` (required): Topic to write about

\- `word\_count` (optional, default: 500): Target word count

\- `tone` (optional, default: "professional"): professional, casual, funny, formal, persuasive



\*\*Example:\*\*

```json

{

&#x20; "campaign\_brief": "sustainable fashion trends 2026",

&#x20; "word\_count": 500

}

```



\---



\### 2. Industry-Specific Blog

\*\*Endpoint:\*\* `POST /generate/industry-blog`



\*\*Parameters:\*\*

\- `campaign\_brief` (required)

\- `industry` (required): tech, fashion, health, food, finance, education, ecommerce, real\_estate

\- `word\_count` (optional, default: 500)

\- `tone` (optional, default: "professional")



\---



\### 3. Tweet Generation

\*\*Endpoint:\*\* `POST /generate/tweets`



\*\*Parameters:\*\*

\- `campaign\_brief` (required)

\- `count` (optional, default: 3): Number of variants (1-10)



\---



\### 4. LinkedIn Post

\*\*Endpoint:\*\* `POST /generate/linkedin`



\*\*Parameters:\*\*

\- `campaign\_brief` (required)

\- `tone` (optional): professional, casual, inspirational, thought\_leadership



\---



\### 5. Email Marketing

\*\*Endpoint:\*\* `POST /generate/email`



\*\*Parameters:\*\*

\- `campaign\_brief` (required)

\- `email\_type` (optional, default: "promotional"): promotional, welcome, newsletter



\---



\### 6. Product Description

\*\*Endpoint:\*\* `POST /generate/product-description`



\*\*Parameters:\*\*

\- `product\_name` (required)

\- `features` (optional): Comma-separated features



\---



\## ⚡ Async Generation (Recommended for Production)



\### Start Async Campaign

\*\*Endpoint:\*\* `POST /async/generate/campaign-with-progress`



\*\*Returns:\*\* `task\_id` immediately



\*\*Example Response:\*\*

```json

{

&#x20; "task\_id": "abc-123-xyz",

&#x20; "status": "PROCESSING",

&#x20; "message": "Campaign generation started"

}

```



\### Check Progress

\*\*Endpoint:\*\* `GET /async/status/{task\_id}`



\*\*Example Response:\*\*

```json

{

&#x20; "status": "PROCESSING",

&#x20; "progress": {

&#x20;   "progress": 60,

&#x20;   "status": "Generating Instagram caption...",

&#x20;   "completed\_steps": \["..."],

&#x20;   "estimated\_time\_remaining": "10s"

&#x20; }

}

```



\### Get Result

\*\*Endpoint:\*\* `GET /async/result/{task\_id}`



\*\*Returns:\*\* Final generated content when complete



\---



\## 🔧 Utility Endpoints



\### Content Quality Analysis

\*\*Endpoint:\*\* `POST /analyze/quality`



\*\*Parameters:\*\*

\- `text` (required): Content to analyze

\- `target\_word\_count` (optional): Expected word count



\*\*Returns:\*\*

\- Readability score

\- Grade level

\- Word count validation

\- Sentence analysis



\---



\### SEO Metadata Generation

\*\*Endpoint:\*\* `POST /generate/seo`



\*\*Parameters:\*\*

\- `text` (required): Content to generate SEO for

\- `campaign\_brief` (required): Topic



\*\*Returns:\*\*

\- Title tag

\- Meta description

\- Keywords

\- URL slug



\---



\### Keyword Extraction

\*\*Endpoint:\*\* `POST /extract/keywords`



\*\*Parameters:\*\*

\- `text` (required)

\- `max\_keywords` (optional, default: 10)



\*\*Returns:\*\*

\- Keywords list

\- Hashtags list



\---



\### List Industries

\*\*Endpoint:\*\* `GET /industries`



\*\*Returns:\*\* Available industry templates



\---



\### Cancel Task

\*\*Endpoint:\*\* `DELETE /async/cancel/{task\_id}`



\*\*Use:\*\* Stop a running async task



\---



\## 📊 Response Formats



\### Success Response

```json

{

&#x20; "success": true,

&#x20; "blog\_post": "Generated content here...",

&#x20; "word\_count": 487,

&#x20; "tone": "professional"

}

```



\### Error Response

```json

{

&#x20; "success": false,

&#x20; "error": {

&#x20;   "message": "Error description",

&#x20;   "solution": "How to fix it",

&#x20;   "code": "ERROR\_CODE"

&#x20; }

}

```



\---



\## 🎯 Best Practices



1\. \*\*For Testing:\*\* Use synchronous endpoints (`/generate/\*`)

2\. \*\*For Production:\*\* Use async endpoints (`/async/generate/\*`)

3\. \*\*For Speed:\*\* Use parallel execution (`/async/generate/campaign-parallel`)

4\. \*\*For Progress:\*\* Use progress tracking (`/async/generate/\*-with-progress`)



\---



\## ⚙️ Configuration



\### Valid Tones

\- professional

\- casual

\- funny

\- formal

\- persuasive



\### Valid Industries

\- tech

\- fashion

\- health

\- food

\- finance

\- education

\- ecommerce

\- real\_estate



\### Limits

\- Min word count: 50

\- Max word count: 2000

\- Min tweet count: 1

\- Max tweet count: 10

\- Task expiration: 1 hour



\---



\## 🆘 Error Codes



\- `CONFIG\_ERROR` - API key missing

\- `CONNECTION\_ERROR` - Failed to connect

\- `RATE\_LIMIT` - API rate limit exceeded

\- `VALIDATION\_ERROR` - Invalid input

\- `GENERATION\_ERROR` - Content generation failed

\- `TIMEOUT\_ERROR` - Request timed out



\---



\*\*Last Updated:\*\* March 22, 2026

\*\*Version:\*\* 1.0.0


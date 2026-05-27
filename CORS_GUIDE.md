# How to Enable CORS for Your API

> 73% of APIs in public-apis cannot be used directly from browsers due to missing CORS headers.
> This guide helps API maintainers fix that.

## What is CORS?

Cross-Origin Resource Sharing (CORS) allows browsers to make requests to APIs on different domains.
Without CORS headers, browser-based applications get blocked by the Same-Origin Policy.

## Quick Fixes by Platform

### Nginx

```nginx
location / {
    add_header Access-Control-Allow-Origin "*" always;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS" always;
    add_header Access-Control-Allow-Headers "Content-Type, Authorization" always;

    # Handle preflight
    if ($request_method = OPTIONS) {
        add_header Access-Control-Allow-Origin "*";
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Content-Type, Authorization";
        add_header Access-Control-Max-Age 86400;
        add_header Content-Length 0;
        add_header Content-Type text/plain;
        return 204;
    }
}
```

### Apache (.htaccess)

```apache
Header set Access-Control-Allow-Origin "*"
Header set Access-Control-Allow-Methods "GET, POST, OPTIONS"
Header set Access-Control-Allow-Headers "Content-Type, Authorization"
```

### Express.js

```javascript
const cors = require('cors');
app.use(cors({
    origin: '*',                    // or ['https://yourapp.com']
    methods: ['GET',POST', 'OPTIONS'],
    allowedHeaders: ['Content-Type', 'Authorization']
}));
```

### FastAPI (Python)

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # or ["https://yourapp.com"]
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Flask (Python)

```python
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

### Node.js (raw)

```javascript
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    if (req.method === 'OPTIONS') return res.sendStatus(204);
    next();
});
```

### API Gateway (AWS API Gateway)

In Method Response → Add header `Access-Control-Allow-Origin`
In Integration Response → Add mapping:

```
# 200
Access-Control-Allow-Origin: '*'
Access-Control-Allow-Methods: 'GET,POST,OPTIONS'
```

### Cloudflare Workers

```javascript
addEventListener('fetch', event => {
    event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
    const response = await fetch(request);
    const headers = new Headers(response.headers);
    headers.set('Access-Control-Allow-Origin', '*');
    headers.set('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
    headers.set('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    return new Response(response.body, { ...response, headers });
}
```

## Security Considerations

- **`*` allows any website to call your API** — fine for public read-only data
- **For authenticated APIs**, use explicit origins: `allow_origins: ['https://yourapp.com']`
- **Credentials**: if you need cookies/auth headers, use `credentials: true` + explicit origin (not `*`)

## Checklist Before Submitting a PR

- [ ] Your API responds to `OPTIONS` preflight requests
- [ ] `Access-Control-Allow-Origin` header is present
- [ ] Test with: `curl -X OPTIONS -I https://your-api.com/endpoint`
- [ ] Update your public-apis entry CORS field from `Unknown` → `Yes`

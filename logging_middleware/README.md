# Logging Middleware

A reusable Python logging middleware that sends log messages to the Affordmed evaluation server.

## Installation

```bash
pip install requests
```

## How to Use

```python
from logger import Log

Log('backend', 'error', 'controller', 'Some error message')
```

## Function Parameters

- **stack**: 'backend' or 'frontend'
- **level**: 'debug', 'info', 'warn', 'error', 'fatal'
- **package**: Package name
- **message**: Log message

## Backend Packages
cache, controller, crud_job, db, domain, auth, config, middleware, utils

## Frontend Packages
api, component, hook, page, state, style, auth, config, middleware, utils

## API Endpoint
http://4.224.186.213/evaluation-service/logs
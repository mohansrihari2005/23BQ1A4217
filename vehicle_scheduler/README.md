# Vehicle Maintenance Scheduler

This is a simple FastAPI application that optimizes vehicle maintenance scheduling.

## How It Works

1. Fetches list of depots (maintenance centers)
2. Fetches list of vehicles needing maintenance
3. Runs optimization algorithm to pick best maintenance tasks
4. Returns optimized schedule

## Installation

```bash
pip install -r requirements.txt
```

## Run the App

```bash
python main.py
```

The app will start at: http://localhost:8000

## API Routes

### Home
```
GET /
```

### Get Schedule
```
GET /schedule
```

Returns depots, vehicles, and optimized schedule.

## Files

- **main.py** - FastAPI application main file
- **controller.py** - Functions to fetch data from APIs
- **optimization.py** - Algorithm to optimize maintenance tasks
- **requirements.txt** - Python dependencies

## How Logging Works

The app logs all events to the test server using the logging middleware.

Example logs:
- "Schedule route called"
- "Fetching depots from API"
- "Fetching vehicles from API"
- "Running optimization algorithm"

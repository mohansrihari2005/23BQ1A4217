from fastapi import FastAPI
import sys
sys.path.append('..')
from logging_middleware.logger import Log
from priority_inbox import getPriorityInbox

app = FastAPI()

@app.get("/")
def home():
    Log('backend', 'info', 'controller', 'Notification app home route called')
    return {"message": "Campus Notifications Microservice"}

@app.get("/notifications/priority")
def priorityInbox(n: int = 10):
    try:
        Log('backend', 'info', 'controller', 'Priority inbox route called')
        notifications = getPriorityInbox(n)
        return {
            "status": "success",
            "count": len(notifications),
            "notifications": notifications
        }
    except Exception as e:
        Log('backend', 'error', 'controller', 'Error: ' + str(e))
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
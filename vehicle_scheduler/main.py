from fastapi import FastAPI
import sys
sys.path.append('..')

from logging_middleware.logger import Log
from controller import getDepots, getVehicles
from optimization import optimizeTasks

app = FastAPI()

@app.get("/")
def home():
    Log('backend', 'info', 'controller', 'Home route called')
    return {"message": "Vehicle Maintenance Scheduler"}

@app.get("/schedule")
def getSchedule():
    try:
        Log('backend', 'info', 'controller', 'Schedule route called')
        
        # Fetch depots
        Log('backend', 'info', 'db', 'Fetching depots from API')
        depots = getDepots()
        
        # Fetch vehicles
        Log('backend', 'info', 'db', 'Fetching vehicles from API')
        vehicles = getVehicles()
        
        # Run optimization
        Log('backend', 'info', 'crud_job', 'Running optimization algorithm')
        result = optimizeTasks(vehicles, depots)
        
        Log('backend', 'info', 'cache', 'Schedule optimized and cached')
        
        return {
            "status": "success",
            "depots": depots,
            "vehicles": vehicles,
            "optimized_schedule": result
        }
    
    except Exception as error:
        Log('backend', 'error', 'controller', 'Error in schedule: ' + str(error))
        return {"status": "error", "message": str(error)}

if __name__ == "__main__":
    Log('backend', 'info', 'controller', 'Vehicle Scheduler app starting')
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

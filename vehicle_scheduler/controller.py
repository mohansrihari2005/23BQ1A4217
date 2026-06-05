import requests
import sys
sys.path.append('..')

from logging_middleware.logger import Log
from config import BEARER_TOKEN, DEPOTS_API, VEHICLES_API

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + BEARER_TOKEN
}

def getDepots():
    """
    Fetch depots from test server and map keys to lowercase
    """
    try:
        Log('backend', 'info', 'controller', 'Calling depots API')
        
        response = requests.get(DEPOTS_API, headers=headers)
        
        if response.status_code == 200:
            depots_raw = response.json()['depots']
            
            # Map uppercase keys to lowercase for consistency
            depots = []
            for depot in depots_raw:
                depots.append({
                    'id': depot.get('ID'),
                    'mechanicHours': depot.get('MechanicHours')
                })
            
            Log('backend', 'info', 'cache', 'Depots fetched and cached: ' + str(len(depots)) + ' depots')
            return depots
        else:
            Log('backend', 'error', 'controller', 'Failed to fetch depots: ' + str(response.status_code))
            return []
    
    except Exception as error:
        Log('backend', 'error', 'db', 'Error fetching depots: ' + str(error))
        return []

def getVehicles():
    """
    Fetch vehicles from test server and map keys to lowercase
    """
    try:
        Log('backend', 'info', 'controller', 'Calling vehicles API')
        
        response = requests.get(VEHICLES_API, headers=headers)
        
        if response.status_code == 200:
            vehicles_raw = response.json()['vehicles']
            
            # Map uppercase keys to lowercase for consistency
            vehicles = []
            for vehicle in vehicles_raw:
                vehicles.append({
                    'taskID': vehicle.get('TaskID'),
                    'duration': vehicle.get('Duration'),
                    'impact': vehicle.get('Impact')
                })
            
            Log('backend', 'info', 'cache', 'Vehicles fetched and cached: ' + str(len(vehicles)) + ' vehicles')
            return vehicles
        else:
            Log('backend', 'error', 'controller', 'Failed to fetch vehicles: ' + str(response.status_code))
            return []
    
    except Exception as error:
        Log('backend', 'error', 'db', 'Error fetching vehicles: ' + str(error))
        return []

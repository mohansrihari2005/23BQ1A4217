import sys
sys.path.append('..')

from logging_middleware.logger import Log

def optimizeTasks(vehicles, depots):
    """
    Simple optimization algorithm to select best maintenance tasks
    
    Algorithm: Greedy approach - sort by impact score and pick best ones that fit budget
    """
    
    try:
        Log('backend', 'debug', 'domain', 'Starting optimization algorithm')
        
        if not depots or len(depots) == 0:
            Log('backend', 'warn', 'domain', 'No depots available')
            return []
        
        # Get first depot's mechanic hours as budget
        depot = depots[0]
        budget = depot['mechanicHours']
        
        Log('backend', 'info', 'domain', 'Budget: ' + str(budget) + ' mechanic hours')
        
        # Sort vehicles by impact score (highest first)
        sorted_vehicles = sorted(vehicles, key=lambda v: v['impact'], reverse=True)
        
        Log('backend', 'debug', 'cache', 'Vehicles sorted by impact score')
        
        # Select vehicles that fit in budget
        selected = []
        total_hours = 0
        total_impact = 0
        
        for vehicle in sorted_vehicles:
            duration = vehicle['duration']
            impact = vehicle['impact']
            
            # Check if this vehicle fits in remaining budget
            if total_hours + duration <= budget:
                selected.append({
                    'taskID': vehicle['taskID'],
                    'duration': duration,
                    'impact': impact
                })
                total_hours += duration
                total_impact += impact
                Log('backend', 'info', 'crud_job', 'Selected vehicle: ' + vehicle['taskID'] + ', Duration: ' + str(duration))
        
        Log('backend', 'info', 'domain', 'Optimization complete. Selected ' + str(len(selected)) + ' vehicles. Total impact: ' + str(total_impact))
        
        return {
            'selected_vehicles': selected,
            'total_duration': total_hours,
            'total_impact': total_impact,
            'budget': budget
        }
    
    except Exception as error:
        Log('backend', 'error', 'domain', 'Error in optimization: ' + str(error))
        return []

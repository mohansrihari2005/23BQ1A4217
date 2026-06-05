import requests
import sys
sys.path.append('..')
from config import BEARER_TOKEN, LOGS_API

def Log(stack, level, package, message):
    """
    Simple logging function that sends logs to test server
    
    Args:
        stack: 'backend' or 'frontend'
        level: 'debug', 'info', 'warn', 'error', 'fatal'
        package: package name (for backend or frontend)
        message: log message
    """
    
    # Validate stack
    if stack not in ['backend', 'frontend']:
        print('Invalid stack value')
        return
    
    # Validate level
    valid_levels = ['debug', 'info', 'warn', 'error', 'fatal']
    if level not in valid_levels:
        print('Invalid level value')
        return
    
    # Validate package for backend
    if stack == 'backend':
        backend_packages = ['cache', 'controller', 'crud_job', 'db', 'domain', 'auth', 'config', 'middleware', 'utils']
        if package not in backend_packages:
            print('Invalid package for backend')
            return
    
    # Validate package for frontend
    if stack == 'frontend':
        frontend_packages = ['api', 'component', 'hook', 'page', 'state', 'style', 'auth', 'config', 'middleware', 'utils']
        if package not in frontend_packages:
            print('Invalid package for frontend')
            return
    
    # Bearer token from config
    token = BEARER_TOKEN
    
    # Create payload
    payload = {
        'stack': stack,
        'level': level,
        'package': package,
        'message': message
    }
    
    # Headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }
    
    # Send log to server
    try:
        response = requests.post(LOGS_API, json=payload, headers=headers)
        
        # Check status code (200 or 201 is success)
        if response.status_code in [200, 201]:
            data = response.json()
            if 'logID' in data:
                print('Log sent successfully')
                print('LogID: ' + data['logID'])
                print('Message: ' + data['message'])
            else:
                print('Log sent but response format unexpected: ' + str(data))
        else:
            print('Error: Server returned status ' + str(response.status_code))
            print('Response: ' + str(response.text))
    except Exception as error:
        print('Error sending log: ' + str(error))

import requests
import sys
sys.path.append('..')
from logging_middleware.logger import Log
from config import BEARER_TOKEN

NOTIFICATIONS_API = "http://4.224.186.213/evaluation-service/notifications"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + BEARER_TOKEN
}

# Weight map: placement > result > event
TYPE_WEIGHT = {
    'Placement': 3,
    'Result': 2,
    'Event': 1
}

def getPriorityInbox(n=10):
    """
    Fetch notifications and return top n by priority
    Priority = type weight + recency score
    """
    try:
        Log('backend', 'info', 'controller', 'Fetching notifications from API')
        
        response = requests.get(NOTIFICATIONS_API, headers=headers)
        
        if response.status_code != 200:
            Log('backend', 'error', 'controller', 'Failed to fetch notifications: ' + str(response.status_code))
            return []
        
        notifications = response.json()['notifications']
        Log('backend', 'info', 'cache', 'Fetched ' + str(len(notifications)) + ' notifications')
        
        # Score each notification
        scored = []
        for i, notif in enumerate(notifications):
            type_score = TYPE_WEIGHT.get(notif.get('Type', ''), 0)
            # Recency: earlier in list = more recent = higher score
            recency_score = len(notifications) - i
            total_score = (type_score * 1000) + recency_score
            
            scored.append({
                'id': notif.get('ID'),
                'type': notif.get('Type'),
                'message': notif.get('Message'),
                'timestamp': notif.get('Timestamp'),
                'score': total_score
            })
        
        # Sort by score descending, return top n
        scored.sort(key=lambda x: x['score'], reverse=True)
        top_n = scored[:n]
        
        Log('backend', 'info', 'domain', 'Returning top ' + str(n) + ' priority notifications')
        return top_n
    
    except Exception as e:
        Log('backend', 'error', 'controller', 'Error in getPriorityInbox: ' + str(e))
        return []
#!/usr/bin/env python3
import requests
import json
import time

print("Testing /schedule endpoint...")
print()

url = "http://localhost:8000/schedule"
print(f"GET {url}")
print()

try:
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    response_time = end_time - start_time
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response_time:.3f} seconds")
    print()
    
    if response.status_code == 200:
        data = response.json()
        print("Response Body:")
        print(json.dumps(data, indent=2))
    else:
        print(f"Error: {response.text}")
        
except Exception as e:
    print(f"Error: {e}")

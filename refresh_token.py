#!/usr/bin/env python3
import requests
import json
from config import CLIENT_ID, CLIENT_SECRET, ACCESS_CODE, USER_EMAIL, USER_NAME, ROLL_NUMBER

print("Refreshing bearer token...")
print(f"CLIENT_ID: {CLIENT_ID}")
print(f"CLIENT_SECRET: {CLIENT_SECRET}")
print(f"ACCESS_CODE: {ACCESS_CODE}")
print(f"USER_EMAIL: {USER_EMAIL}")
print(f"USER_NAME: {USER_NAME}")
print(f"ROLL_NUMBER: {ROLL_NUMBER}")
print()

# Phase 2: Get Bearer Token
AUTH_URL = "http://4.224.186.213/evaluation-service/auth"

auth_payload = {
    "clientID": CLIENT_ID,
    "clientSecret": CLIENT_SECRET,
    "accessCode": ACCESS_CODE,
    "email": USER_EMAIL,
    "name": USER_NAME,
    "rollNo": ROLL_NUMBER
}

print(f"POST to: {AUTH_URL}")
print(f"Payload: {json.dumps(auth_payload, indent=2)}")
print()

try:
    response = requests.post(AUTH_URL, json=auth_payload)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 201:
        data = response.json()
        if 'access_token' in data:
            token = data['access_token']
            print(f"\n✓ New Token Obtained!")
            print(f"Token: {token[:50]}...\n")
            
            # Update config.py
            print("Updating config.py...")
            with open('config.py', 'r') as f:
                lines = f.readlines()
            
            # Find and replace the BEARER_TOKEN line
            new_lines = []
            for line in lines:
                if line.startswith('BEARER_TOKEN = '):
                    new_lines.append(f'BEARER_TOKEN = "{token}"\n')
                else:
                    new_lines.append(line)
            
            with open('config.py', 'w') as f:
                f.writelines(new_lines)
            
            print("✓ config.py updated with new token!")
        else:
            print(f"Unexpected response format: {data}")
    else:
        print(f"Failed with status {response.status_code}: {data}")
except Exception as e:
    print(f"Error: {e}")

#!/usr/bin/env python3
import requests
import json
from config import BEARER_TOKEN, LOGS_API, DEPOTS_API

print("Testing API connection...")
print(f"Bearer Token: {BEARER_TOKEN[:50]}...")
print(f"LOGS_API: {LOGS_API}")
print()

# Test 1: Test LOGS_API
print("Test 1: Testing LOGS_API")
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + BEARER_TOKEN
}
payload = {
    'stack': 'backend',
    'level': 'info',
    'package': 'controller',
    'message': 'Test message'
}

try:
    response = requests.post(LOGS_API, json=payload, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "="*60 + "\n")

# Test 2: Test DEPOTS_API
print("Test 2: Testing DEPOTS_API")
try:
    response = requests.get(DEPOTS_API, headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:200]}...")
except Exception as e:
    print(f"Error: {e}")

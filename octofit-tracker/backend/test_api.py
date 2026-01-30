#!/usr/bin/env python3
import requests
import json

base_url = "http://localhost:8000/api"

print("=" * 60)
print("OctoFit Tracker API Verification")
print("=" * 60)

endpoints = [
    ("/", "API Root"),
    ("/teams/", "Teams"),
    ("/users/", "Users"),
    ("/activities/", "Activities"),
    ("/workouts/", "Workouts"),
    ("/leaderboard/", "Leaderboard"),
]

for endpoint, name in endpoints:
    try:
        response = requests.get(f"{base_url}{endpoint}")
        print(f"\n{name} ({endpoint}):")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list):
                print(f"Count: {len(data)}")
                if len(data) > 0:
                    print(f"Sample: {json.dumps(data[0], indent=2)}")
            else:
                print(f"Data: {json.dumps(data, indent=2)}")
    except Exception as e:
        print(f"\n{name} ({endpoint}): ERROR - {e}")

print("\n" + "=" * 60)

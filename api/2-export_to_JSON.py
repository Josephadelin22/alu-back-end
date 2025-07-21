#!/usr/bin/python3
"""
Exports all tasks for a given employee to a JSON file.
Usage: python3 2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        sys.exit(1)

    user = user_response.json()
    employee_username = user.get("username")

    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Build the list of task dicts as required
    task_list = []
    for task in todos:
        task_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        })

    json_data = {str(employee_id): task_list}
    filename = "{}.json".format(employee_id)

    with open(filename, mode='w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile)

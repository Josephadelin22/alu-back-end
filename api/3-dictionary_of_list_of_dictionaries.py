#!/usr/bin/python3
"""
Exports all tasks from all employees to a JSON file.
Usage: python3 3-dictionary_of_list_of_dictionaries.py
"""

import json
import requests

if __name__ == "__main__":
    # Get all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    # Prepare a dictionary: {user_id: [ {username, task, completed}, ... ]}
    all_tasks = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        # List of todos for this user
        user_tasks = []
        for task in todos:
            if task.get("userId") == user.get("id"):
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        all_tasks[user_id] = user_tasks

    # Write to todo_all_employees.json
    with open("todo_all_employees.json", "w", encoding="utf-8") as jsonfile:
        json.dump(all_tasks, jsonfile)


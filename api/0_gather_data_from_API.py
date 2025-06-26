#!/usr/bin/python3


import requests
import sys


if _name_ == "_main_":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_API <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)


    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com?todos?userId={employee_id}"


    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error:Failed to retrieve data from API")
        sys.exit(1)

    employee_name = user_response.json().get('name')
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get('completed') is True]
    number_done = len(done_tasks)


    print(f"Employee {employee_name} is done with tasks({number_done}/{totals_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")





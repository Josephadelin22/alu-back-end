#!/usr/bin/python3
"""
Exports all tasks for a given employee to a CSV file.
Usage: python3 1-export_to_CSV.py <employee_id>
"""

import CSV
import requests 
import sys 

if __name__ == "__main__":

    if len(sys.argv) != 2:
       print("Usage: {} <employee_id>".format(sys.argv[0]))
       sys.exit(1)
    
    try:
       
       employee_id = int()sys.argv[1])


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


    filename = "{}.csv".format(employee_id)
    
    with open(filename, mode='w', newline ='', encoding='utf-8') as csvfile:
        writer = csv.writer(csv, quoting=csv.QUOTE_ALL)
        
        for task in todos:
	    writer.writerow([
employee_id,
employee_username,
task.get("completed"),
task.get("title")
])        

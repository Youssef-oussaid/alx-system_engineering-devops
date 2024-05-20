#!/usr/bin/python3
"""A module to get amployee data using api"""

import requests
import sys

def get_employee_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()

def get_todo_list(username):
    todo_url = f"https://jsonplaceholder.typicode.com/todos?username={username}"
    response_todo = requests.get(todo_url)
    return response_todo.json()

def print_todo_progress(employee_id):
    employee_data = get_employee_data(employee_id)
    username = employee_data['username']
    todo_data = get_todo_list(username)
    
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])

    print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    print_todo_progress(employee_id)

#!/usr/bin/python3
"""module that get's the todo list of a user and displayes
   the completed task and it's name
"""


import json
import requests
from sys import argv


def count_done_tasks(tasks):
    """count_done_tasks
    counts the already done tasks in a dict
    @tasks: the tasks dict
    """
    completed_tasks = []
    for val in tasks:
        if val.get("completed") is True:
            completed_tasks.append(val.get("title"))
    return completed_tasks


def get_user_data(id):
    """get_user_data
    sends a get requests to an api to get todos of a users with an id
    @id: the user id
    """
    # get the todos
    request_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos/"
    req1 = requests.get(request_url)
    todos = json.loads(req1.text)

    # get user data
    req2 = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    user = json.loads(req2.text)
    return (todos, user)


def driver():
    """driver
    this is the driver function for calling other methods
    """
    # arg validation
    if len(argv) != 2:
        return
    try:
        id = int(argv[1])
    except Exception:
        return
    # get data
    todos, user = get_user_data(id)
    # get count of done tasks
    titles = count_done_tasks(todos)

    print(f"Employee {user.get('name')}", end="")
    print(f"is done with tasks({len(titles)}/{len(todos)}):")
    for done_task in titles:
        print(f"\t {done_task}")


if __name__ == "__main__":
    driver()

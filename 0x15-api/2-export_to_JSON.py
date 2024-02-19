#!/usr/bin/python3
"""module that get's the todo list of a user and save
   in a csv file
"""

import csv
import json
import requests
from sys import argv


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


def format_to_json(USER_ID, USER_NAME, todos):
    """format_to_json
    format the data from the api into a json format (again), and save
    it in a json file
    """
    master_dict = {}
    master_dict[USER_ID] = []
    for todo in todos:
        tmp_dict = {}
        tmp_dict["task"] = todo.get("title")
        tmp_dict["completed"] = todo.get("completed")
        tmp_dict["username"] = USER_NAME
        master_dict[USER_ID].append(tmp_dict)
    with open(f"{USER_ID}.json", "w") as file:
        file.write(json.dumps(master_dict))


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
    todos, user = get_user_data(argv[1])
    format_to_json(user.get("id"),
                   user.get("username"),
                   todos)


if __name__ == "__main__":
    driver()

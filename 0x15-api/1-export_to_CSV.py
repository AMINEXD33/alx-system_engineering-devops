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
    with open(f'{id}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile,
                            delimiter=',',
                            quotechar='|',
                            quoting=csv.QUOTE_MINIMAL)
        username = user.get("username")
        id = user.get("id")

        for element in todos:
            writer.writerow([f'"{id}"',
                             f'"{username}"',
                             f'"{element.get("completed")}"',
                             f'"{element.get("title")}"']
                            )


if __name__ == "__main__":
    driver()

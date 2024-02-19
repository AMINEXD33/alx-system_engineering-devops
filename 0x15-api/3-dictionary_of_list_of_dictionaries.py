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

    return todos


def get_available_users():
    """get_available_users
    not to use brute forcing to get all users, but
    rather we're going to use the api response as
    a reference
    """
    verified_user_ids = []
    verified_usernames = []
    request_url = f"https://jsonplaceholder.typicode.com/users"
    req1 = requests.get(request_url)
    users = json.loads(req1.text)
    for user in users:
        try:
            verified_user_ids.append(int(user["id"]))
            verified_usernames.append(user["username"])
        except IndexError:
            break
    return (verified_user_ids, verified_usernames)


def format_to_json(USER_NAME, todo):
    """format_to_json
    format the data from the api into a json format (again), and save
    it in a json file
    """
    tmp_dict = {}
    tmp_dict["username"] = USER_NAME
    tmp_dict["task"] = todo.get("title")
    tmp_dict["completed"] = todo.get("completed")
    return (tmp_dict)


def driver():
    """driver
    this is the driver function for calling other methods
    """
    verifed_users, verified_usernames = get_available_users()
    master_dict = {}
    for user in range(len(verifed_users)):
        todos = get_user_data(verifed_users[user])
        master_dict[verifed_users[user]] = []
        for user_todo in todos:
            master_dict[verifed_users[user]]\
                .append(format_to_json(verified_usernames[user], user_todo))
    with open("todo_all_employees.json", "w") as file:
        file.write(json.dumps(master_dict))


if __name__ == "__main__":
    driver()

import requests
import json
from sys import argv


def count_done_tasks(tasks):
    """count_done_tasks
    counts the already done tasks in a dict
    """
    completed_tasks = []
    for val in tasks:
        if val["completed"] is True:
            completed_tasks.append(val["title"])
    return completed_tasks


def get_user_data(id):
    """get_user_data
    sends a get requests to an api to get todos of a users with an id
    @id: the user id
    """
    # get the todos
    req1 = requests.get(f"https://jsonplaceholder.\
    typicode.com/users/{id}/todos/")
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
        return None
    try:
        id = int(argv[1])
    except Exception:
        return None
    # get data
    todos, user = get_user_data(id)
    # get count of done tasks
    titles = count_done_tasks(todos)
    #
    print(f"Employee {user['name']} \
    is done with tasks({len(titles)}/{len(todos)}):")
    for done_task in titles:
        print(f"\t {done_task}")


driver()

from flask import Flask, request, jsonify
import requests
import time
import random

app = Flask(__name__)

ORDER_ID = 1
tables = [{"tableID": 1, "orders": "2"}, {"tableID": 2, "orders": "3"}]
foods = [{"id": 1, "name": "pizza", "preparation-time": 20, "complexity": 2, "cooking-apparatus": "oven"},
         {"id": 2, "name": "salad", "preparation-time": 10, "complexity": 1, "cooking-apparatus": None},
         {"id": 3, "name": "zeama", "preparation-time": 7, "complexity": 1, "cooking-apparatus": "stove"},
         {"id": 4, "name": "Scallop", "preparation-time": 32, "complexity": 3, "cooking-apparatus": None},
         {"id": 5, "name": "Island Duck", "preparation-time": 35, "complexity": 3, "cooking-apparatus": "oven"},
         {"id": 6, "name": "Waffles", "preparation-time": 10, "complexity": 1, "cooking-apparatus": "stove"},
         {"id": 7, "name": "Aubergine", "preparation-time": 20, "complexity": 2, "cooking-apparatus": None},
         {"id": 8, "name": "Lasagna", "preparation-time": 30, "complexity": 2, "cooking-apparatus": "oven"},
         {"id": 9, "name": "Burger", "preparation-time": 15, "complexity": 1, "cooking-apparatus": "oven"},
         {"id": 10, "name": "Gyros", "preparation-time": 15, "complexity": 1, "cooking-apparatus": None}]
orders = []


class Table:
    def __init__(self, state):
        self.state = state

    def generate_order(self):
        max_wait_time = 0
        items = []
        for _ in range(1, random.randint(1, 5)):
            items.append(random.randint(1, 10))
        for item in items:
            if max_wait_time < foods[item]["preparation-time"]:
                max_wait_time = foods[item]["preparation-time"]
        order = {"id": ORDER_ID, "items": items, "priority": random.randint(1, 5), "max_wait": max_wait_time * 1.3}
        wait_time = random.randint(1, 5)
        self.change_state(wait_time)

    def change_state(self, wait_time):
        if self.state != 3:
            self.state += 1
            time.sleep(wait_time)


class Waiters:
    def __init__(self):
        pass

    def pick_order(self, wait_time):
        pass

    def send_order(self):
        pass


@app.route('/kitchen_data')
def hello_world():
    url = "http://172.18.0.2:8080/app?id=1"
    return requests.get(url).text


@app.route('/app')
def id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Unknown request for dinning hall"

    result = []

    for table in tables:
        if table["tableID"] == id:
            result.append(table)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

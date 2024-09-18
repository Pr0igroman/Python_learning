import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

with open("json_to_csv.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
    writer.writeheader()
    for i in todos:
        writer.writerow(i)
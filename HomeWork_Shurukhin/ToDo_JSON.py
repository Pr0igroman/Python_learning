import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    if todo["completed"]:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1
# print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)

max_complete = top_users[0][1]
# print(max_complete)

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))


#
# max_users = " and ".join(users)
# print(max_users)
# print(f"Users {max_users} completed {max_complete} Todos")

def save_filtered_data():
    filtered_data = [item for item in todos if str(item['userId']) in users and item["completed"]]

    with open("filter_data.json", "w") as f:
        json.dump(filtered_data, f, indent=4)

    print("Сохранение завершено!")


save_filtered_data()

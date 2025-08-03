import json

tasks = []

try:
    with open("todo.json", "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("What do you want to do?")
    print("1. Add task")
    print("2. Show tasks")
    print("3. Mark done")
    print("4. Exit")
    x = input("Enter: ")

    if x == "1":
        t = input("Enter your task: ")
        task = {}
        task['description'] = t
        task['done'] = False
        tasks.append(task)
        with open("todo.json", "w") as f:
            json.dump(tasks, f)

    elif x == "2":
        n = 1
        for task in tasks:
            if task['done']:
                status = "Done"
            else:
                status = "Not done"
            print(str(n) + ". " + task['description'] + " [" + status + "]")
            n = n + 1

    elif x == "3":
        i = int(input("Which number? "))
        tasks[i-1]['done'] = True
        with open("todos.json", "w") as f:
            json.dump(tasks, f)
        print("Marked as done")

    elif x == "4":
        break

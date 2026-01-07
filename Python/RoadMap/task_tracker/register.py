import json 
import os

from task_status import TaskStatus

def create_register():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
        file.close() 
    
def add_task(description, createdAt):
    create_register()
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    new_task = {
        "id": len(tasks)+1,
        "description": description,
        "status": TaskStatus.TODO.value,
        "createdAt": createdAt,
        "updatedAt": None,
    }
    tasks.append(new_task)
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    file.close()
    return new_task['id']

create_register()
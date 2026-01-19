from datetime import datetime

from register import add_task, get_tasks

def create_task(description):
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task = add_task(description, register_date)
    return f"Task created successfully with id: {task}"

def list_tasks():
    tasks = get_tasks()
    for task in tasks:
        print(task)
    return


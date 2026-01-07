from datetime import datetime

from register import add_task

def create_task(description):
    register_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    task = add_task(description, register_date)
    return f"Task created successfully with id: {task}"
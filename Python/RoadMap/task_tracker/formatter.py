def format_tasks(tasks):
    """Format a list of tasks for display."""
    if not tasks:
        return "No tasks found."

    output = []
    for task in tasks:
        output.append(f"ID: {task['id']}")
        output.append(f"Title: {task.get('title', '')}")
        output.append(f"Description: {task['description']}")
        output.append(f"Status: {task['status']}")
        output.append(f"Created At: {task['createdAt']}")
        if task.get("updatedAt"):
            output.append(f"Updated At: {task['updatedAt']}")
        output.append("-" * 20)
    return "\n".join(output)

from argparse import ArgumentParser

from tasks import TaskTracker


def main():
    parser = ArgumentParser(description="Task tracker command line interface")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Create a new task")
    add_parser.add_argument("--title", help="Task title")
    add_parser.add_argument("--description", required=True, help="Task description")


    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument(
        "--status",
        choices=["to-do", "in-progress", "done"],
        help="Filter tasks by status",
    )

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in-progress"
    )
    mark_in_progress_parser.add_argument("--id", type=int, required=True, help="Task id")

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("--id", type=int, required=True, help="Task id")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("--id", type=int, required=True, help="Task id")
    update_parser.add_argument("--title", help="New task title")
    update_parser.add_argument(
        "--description", required=True, help="New task description"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("--id", type=int, required=True, help="Task id")

    describe_parser = subparsers.add_parser("describe", help="Show task details")
    describe_parser.add_argument("--id", type=int, required=True, help="Task id")

    args = parser.parse_args()
    tracker = TaskTracker()

    if args.command == "add":
        print(tracker.create_task(args.title, args.description))
    elif args.command == "list":
        tasks = (
            tracker.list_tasks_status(args.status)
            if args.status
            else tracker.list_tasks()
        )
        print(tracker.format_tasks(tasks))
    elif args.command == "mark-in-progress":
        print(tracker.mark_task_in_progress(args.id))
    elif args.command == "mark-done":
        print(tracker.mark_task_done(args.id))
    elif args.command == "update":
        print(tracker.update_task(args.id, args.title, args.description))
    elif args.command == "delete":
        print(tracker.delete_task(args.id))
    elif args.command == "describe":
        task = tracker.describe_task(args.id)
        if task:
            print(tracker.format_tasks([task]))
        else:
            print(f"Task with id {args.id} not found.")



if __name__ == "__main__":
    main()

from argparse import ArgumentParser

from tasks import create_task, list_tasks

def main():
    parser = ArgumentParser()
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--description", help="Task description")
    parser.add_argument("--id", help="Task id")
    subparser = parser.add_subparsers()
    list_parser = subparser.add_parser("todo", help="List tasks in to-do status")
    list_parser = subparser.add_parser("in-progress", help="List tasks in in-progress status")
    list_parser = subparser.add_parser("done", help="List tasks in done status")
    list_parser.add_argument("list", help="Filter by all tasks", nargs='?')

    parser.add_argument("action", choices=["add", "mark-in-progress", "mark-done", "update"], help="Action to perform")
    args = parser.parse_args()

    if args.action == "add":
        print(create_task(args.description))
    elif args.action == "mark-in-progress":
        pass
    elif args.action == "delete":
        pass
    elif args.action == "list":
        list_tasks()
    elif args.action == "describe":
        pass
    elif args.action == "update":
        pass

if __name__ == "__main__":
    main()

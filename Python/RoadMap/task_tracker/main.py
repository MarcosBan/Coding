from argparse import ArgumentParser

from tasks import create_task

def main():
    parser = ArgumentParser()
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--description", help="Task description")
    parser.add_argument("--due_date", help="Task due date")
    parser.add_argument("--id", help="Task id")

    parser.add_argument("action", choices=["add", "mark-in-progress", "mark-done", "list", "update"], help="Action to perform")
    args = parser.parse_args()

    if args.action == "add":
        print(create_task(args.description))
    elif args.action == "mark-in-progress":
        pass
    elif args.action == "delete":
        pass
    elif args.action == "list":
        pass
    elif args.action == "describe":
        pass
    elif args.action == "update":
        pass

if __name__ == "__main__":
    main()

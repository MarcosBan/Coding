from argparse import ArgumentParser

from expenses import create_expense, update_expense, delete_expense, list_expenses, total_expenses

def main():
    parser = ArgumentParser()
    parser.add_argument("--description", help="Expense description")
    parser.add_argument("--amount", type=float, help="Expense amount")
    parser.add_argument("--month", help="Expense date")
    parser.add_argument("--id", help="Expense id")

    parser.add_argument("action", choices=["add", "update", "delete", "describe", "list", "summary"], help="Action to perform")
    args = parser.parse_args()

    if args.action == "add":
        print(create_expense(args.description, args.amount))
    elif args.action == "update":
        print(update_expense(args.id, args.description, args.amount))
    elif args.action == "delete":
        print(delete_expense(args.id))
    elif args.action == "list":
        expenses = list_expenses()
        for expense in expenses:
            print(f"ID: {expense['id']}, Description: {expense['description']}, Amount: {expense['amount']}")
    elif args.action == "summary":
        print(total_expenses(args.month))

if __name__ == "__main__":
    main()

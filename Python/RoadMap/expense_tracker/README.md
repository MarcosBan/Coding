# Expense Tracker

A small command-line expense tracker. Use the CLI to add, update, delete, list and summarize expenses.

## Usage

Run the CLI script (example filename: `main.py`) with an action and optional flags:

```bash
python main.py <action> [--description DESCRIPTION] [--amount AMOUNT] [--month MONTH] [--id ID]
```

## Actions

- **add**: Create a new expense. Requires `--description` and `--amount`. `--month` is optional.
- **update**: Update an existing expense. Requires `--id`. Use `--description` and/or `--amount` to change fields.
- **delete**: Remove an expense. Requires `--id`.
- **list**: Print all expenses.
- **summary**: Print the total expenses for a given `--month`. If `--month` is omitted, behavior depends on implementation (may return total for all time).
- **describe**: (present in CLI choices) Not handled by the example dispatcher; may be reserved for showing a single expense by id.

## Flags

- `--description`: Expense description (string).
- `--amount`: Expense amount (float).
- `--month`: Expense month/date (string). The format is implementation dependent (e.g. "2025-12" or "December").
- `--id`: Expense id (used by `update` and `delete`).

## Examples

Add a new expense:

```bash
python main.py add --description "Coffee" --amount 3.50 --month "12"
```

Update an expense:

```bash
python main.py update --id 123 --description "Coffee (work)" --amount 4.00
```

Delete an expense:

```bash
python main.py delete --id 123
```

List all expenses:

```bash
python main.py list
```

Get summary for a month:

```bash
python main.py summary --month "2025-12"
```

## Output

The CLI prints the return value of the underlying functions. Typical outputs include confirmation strings or JSON-like expense records. For `list`, each expense is printed in the format:

```
ID: <id>, Description: <description>, Amount: <amount>
```

## Notes

- The CLI relies on an `expenses` module with functions: `create_expense`, `update_expense`, `delete_expense`, `list_expenses`, and `total_expenses`.
- If you see an action in the CLI choices but no corresponding behavior (for example `describe`), check `main.py` to confirm whether that action is implemented.
- Adjust `python main.py` to the actual script filename if different.


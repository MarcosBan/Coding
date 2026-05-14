# Task Tracker

A small command-line task tracker that stores tasks in `tasks.json`.

## Usage

Run commands from the `task_tracker` folder with Python:

```bash
python main.py add --description "Write unit tests"
python main.py add --title "Review" --description "Review pull requests"
python main.py list
python main.py list --status "to-do"
python main.py mark-in-progress --id 1
python main.py mark-done --id 1
python main.py update --id 1 --description "Write integration tests"
python main.py delete --id 1
python main.py describe --id 1
```

## Available commands

- `add` — create a new task
- `list` — show tasks, optionally filtered by status
- `mark-in-progress` — move a task to `in-progress`
- `mark-done` — move a task to `done`
- `update` — change a task title or description
- `delete` — remove a task
- `describe` — show the details of a single task

## Task status values

- `to-do`
- `in-progress`
- `done`

## Notes

Tasks are saved to `tasks.json` in the same folder as `main.py`.
If the file does not exist, it is created automatically.

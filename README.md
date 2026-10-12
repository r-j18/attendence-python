# Attendance Tracker

A command-line attendance tracker written in Python. Add your subjects, mark yourself present or absent, and check your attendance percentage. Data is stored in a local JSON file, so it persists between runs.

No external dependencies. Only the Python standard library is used.

## Requirements

- Python 3

## Setup

```bash
git clone <your-repo-url>
cd <repo-folder>
```

## Usage

Run all commands from the project root:

```bash
python3 main.py <subject> <command>
```

| Command   | What it does                                      |
|-----------|---------------------------------------------------|
| `add`     | Add a new subject (starts at 0 present, 0 absent) |
| `present` | Mark one lecture as attended                      |
| `absent`  | Mark one lecture as missed                        |
| `show`    | Show the attendance percentage                    |
| `rem`     | Remove the subject                                |

### Examples

```bash
python3 main.py DBMS add
python3 main.py DBMS present
python3 main.py DBMS absent
python3 main.py DBMS show
python3 main.py DBMS rem
```

Subject names with spaces need quotes:

```bash
python3 main.py "Data Structures" add
```

### Notes

- Subject names are case-insensitive: `dbms` and `DBMS` refer to the same subject.
- Adding a subject that already exists, or using one that doesn't exist, prints an error and leaves your data untouched.
- An unknown command is rejected with an error message.
- If the data file is corrupted or unreadable, the program stops without overwriting it.

## Data storage

Attendance is saved in `data/data.json`. The file is created on the first save. Each subject is stored as:

```json
{"name": "DBMS", "present": 8, "absent": 2}
```

You can back this file up or edit it by hand. Keep the three field names exactly as shown, and use non-negative whole numbers for the counts.

## Project structure

```
.
├── main.py       # entry point, calls cli.run()
├── cli.py        # parses commands, calls logic and rw, prints output
├── logic.py      # attendance rules: find, add, remove, mark, percentage
├── rw.py         # reads and writes data/data.json
├── classes.py    # Subject class (name, present, absent)
└── data/
    └── data.json # saved attendance
```

Dependencies only point one way: `main → cli → logic / rw → classes`. `logic` never prints and never touches the file, and `rw` is the only module that reads or writes the data file.

## Limitations

- Not packaged for `pip install` yet. Run it from the project root as shown above.
- Percentages are calculated as `present / (present + absent) * 100`. A subject with no records shows 0.

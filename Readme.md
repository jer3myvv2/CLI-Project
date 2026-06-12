# Project Management CLI

A simple command-line application for creating, viewing, editing, and deleting users and projects.

## Requirements

- Python 3.14+
- pip

## Setup

1. Open the project folder.
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

If you do not yet have a requirements.txt file, install the package used by the CLI:

```bash
pip install rich
```

## Run the CLI

From the project root, run:

```bash
python main.py
```

## How to use the menu

The CLI will show this menu:

1. Create User
2. Create Project
3. View Projects by User
4. Edit User
5. Delete User
6. Edit Project
7. Delete Project
8. Exit

### Option 1: Create User
- Enter a user ID.
- Enter the user name.
- The user will be saved to `data/users.json`.

### Option 2: Create Project
- Enter the user ID that owns the project.
- Enter a project ID.
- Enter the project name.
- Enter the project description.
- The project will be saved to `data/projects.json`.

### Option 3: View Projects by User
- Enter a user ID.
- The CLI will display all projects linked to that user.

### Option 4: Edit User
- Enter the user ID to update.
- Enter the new name.
- Leave the name blank to keep the current value.

### Option 5: Delete User
- Enter the user ID to remove.
- The user will be deleted from `data/users.json`.

### Option 6: Edit Project
- Enter the project ID to update.
- Enter the new project name if you want to change it.
- Enter the new description if you want to change it.
- Enter a new user ID if you want to move the project to another user.

### Option 7: Delete Project
- Enter the project ID to remove.
- The project will be deleted from `data/projects.json`.

### Option 8: Exit
- Close the CLI application.

## Data files

The application stores data in these files:

- `data/users.json`
- `data/projects.json`

## Testing

Run the tests with:

```bash
pytest
```

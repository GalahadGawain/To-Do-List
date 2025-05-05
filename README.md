# 📝 To-Do List Manager

A simple, console-based To-Do List application written in Python. This tool allows users to manage their daily tasks efficiently with options to add, view, mark as complete, and delete tasks, all stored persistently in a JSON file.

## 📁 Project Structure

```
.
├── to_do_list.py         # Main application logic
└── todo_list.json        # Task data storage in JSON format
```

## ⚙️ Features

- ✅ View current tasks and their statuses (Pending / Completed)
- ➕ Add new tasks with descriptions
- ✔️ Mark existing tasks as completed
- 🗑️ Delete tasks
- 💾 Persistent data storage using a JSON file

## ▶️ Getting Started

### Prerequisites

- Python 3.x installed
- Terminal or Command Prompt access

### Running the Program

```bash
python to_do_list.py
```

### Example

```bash
 To-Do List Manager
 ====================
1. View Tasks
2. Add Task
3. Complete Task
4. Delete Task
5. Exit
```

## 📦 Data Format

Tasks are stored in `todo_list.json` as follows:

```json
{
  "tasks": [
    {
      "description": "Test 01",
      "complete": false
    },
    {
      "description": "Test 02",
      "complete": true
    }
  ]
}
```

## 🚧 Future Improvements

- Add date/time stamps to tasks
- Implement search/filter functionality
- Create a GUI version using `tkinter` or `PyQt`
- Add unit tests for critical functions

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

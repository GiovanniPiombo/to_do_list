# 📝 To-Do List (Terminal Edition)

A simple **command-line to-do list app**, written in Python, to help manage daily tasks through a clean and colorful terminal interface.

## 🚀 Features

- ✅ Add new tasks  
- 👀 View all tasks with status (completed / not completed)  
- ✔️ Mark tasks as completed  
- ❌ Remove tasks  
- 💾 Save task list to a JSON file  
- 📂 Load task list from a JSON file  

## 📦 Requirements

- Python 3.6 or higher
- [colorama](https://pypi.org/project/colorama/)
- [pyfiglet](https://pypi.org/project/pyfiglet/)

Install dependencies with:

```bash
pip install colorama pyfiglet
```

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/GiovanniPiombo/to_do_list.git
cd to_do_list
```

To start the app:

```bash
python to_do_list.py
```

## 💾 Save & Load

- You can **save** your current to-do list to a `.json` file.
- You can **load** it later to resume from where you left off.

## 📁 Data Structure

Tasks are stored as key/value pairs in a Python dictionary:

```python
{
    "Buy milk": "not done yet",
    "Study Python": "done"
}
```

## 🛠️ Future Improvements (Ideas)

- Task sorting
- GUI version
- Task priorities and due dates
- Auto-backup system

## 📄 License

This project was built for learning purposes. Feel free to use, modify, and share it!

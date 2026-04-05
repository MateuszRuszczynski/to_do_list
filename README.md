# ✅ TaskFlow — Django To-Do Manager

A clean, full-featured task management web application built with Django. Organise your work with tasks, deadlines, and tags — all in one place.

---

## 📋 Features

- **Task list** — view all tasks ordered by status (pending first) then by date
- **Create, edit, delete** tasks and tags
- **Complete / Undo** — toggle a task's done status with a single click
- **Deadlines** — optionally assign a due date and time to any task
- **Tags** — label tasks with multiple tags; one tag can belong to many tasks
- **Persistent sidebar** — navigation visible on every page
- **Fixture** — pre-loaded sample data to get started instantly

---

## 🚀 Getting Started

### 1. Clone or download the project

```bash
git clone https://github.com/MateuszRuszczynski/to_do_list
cd to_do_list
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. (Optional) Load sample data

```bash
python manage.py loaddata task_manager/fixuters/initial_data.json
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open your browser at **http://127.0.0.1:8000/**

---

## 🛠️ Tech Stack

- **Backend** — Python 3.12, Django 5.x
- **Database** — SQLite (default, zero config)
- **Frontend** — Django templates, vanilla CSS
- **Fonts** — DM Serif Display + DM Sans (Google Fonts)

---

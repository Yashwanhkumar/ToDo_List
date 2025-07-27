# ToDo_List

A simple To-Do List web application built with Python (Django/Flask) to manage tasks efficiently.

## Features
- Add, update, and delete tasks
- Simple and clean interface with HTML templates
- Stores task data with SQLite

## Project Structure

- `ToDo/` - Core application code
- `Todo_App/` - Additional app code
- `templates/` - HTML templates
- `db.sqlite3` - SQLite database file
- `manage.py` - Project management script

## Requirements

- Python 3.x
- Django (or Flask)
- Other Python libraries (see requirements.txt if present)

## Setup

1. **Clone the repo:**
git clone https://github.com/Yashwanhkumar/ToDo_List.git
cd ToDo_List

text

2. **(Recommended) Set up virtual environment:**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install requirements:**
pip install -r requirements.txt

text
Or
pip install django

text

4. **Apply migrations:**
python manage.py migrate

text

5. **Run server:**
python manage.py runserver

text

6. **Visit:** `http://127.0.0.1:8000`

## Usage

- Add, edit, and delete tasks via the web interface. Data is saved in the local database.

## Author

Yashwanhkumar

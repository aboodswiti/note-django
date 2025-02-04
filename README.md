# Django Notes API

## Project Overview

This is a simple Django-based REST API for managing notes. The application allows users to create, and retrieve, through a set of API endpoints.

## Features

- Create new notes
- List all notes
- Retrieve a specific note by ID
- Delete a note

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Django 3.2 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/aboodswiti/note-django.git
cd note-django
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install django
```

## Database Setup

1. Apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## API Endpoints

### List Notes
- **URL:** `/api/notes/`
- **Method:** `GET`
- **Response:** JSON array of notes

### Create Note
- **URL:** `/api/notes/`
- **Method:** `POST`
- **Request Body:** 
```json
{
    "title": "Note Title",
    "content": "Note Content"
}
```

### Get Note Details
- **URL:** `/api/notes/<id>/`
- **Method:** `GET`
- **Response:** Note details



## Error Handling

- Invalid data submission returns a 400 Bad Request
- Attempting to retrieve a non-existent note returns a 404 Not Found


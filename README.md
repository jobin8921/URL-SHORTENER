# URL Shortener Application

A URL Shortener application built with **Django** for the backend and **React** for the frontend.  
It allows users to shorten long URLs, copy the shortened link with one click, and generate QR codes for easy sharing.

---

## Features
- Shorten long URLs into concise links
- One-click copy to clipboard
- Generate QR code for each shortened URL
- Simple, clean UI

---

## Tech Stack
- **Backend**: Django (Python 3.x)
- **Frontend**: React.js
- **Database**: SQLite (default), configurable to others
- **Dependencies**: Listed in `requirements.txt` and `package.json`

---

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python 3.x](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/)
- [Git](https://git-scm.com/)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

cd backend
python -m venv venv
# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

# Start backend server
python manage.py runserver

## frontend server run

cd frontend
npm install
npm start




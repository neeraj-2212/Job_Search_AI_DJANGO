# Job Search AI – Resume Analyzer (Django)

A Django web application that helps candidates analyze their resume and find relevant jobs. [One line on what the user gets, e.g. "Upload a resume and get an analysis with job suggestions."]

## Features

- [User registration and login]
- [Resume upload (PDF/DOCX)]
- [Resume analysis / score / suggestions]
- [Job search or job recommendations]
- [Admin panel for managing users and data]

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, [JavaScript / Bootstrap]
- **Database:** [SQLite / MySQL / PostgreSQL]

## Screenshots

![Home Page](screenshots/home.png)
![Resume Analysis](screenshots/analysis.png)

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/neeraj-2212/Job_Search_AI_DJANGO.git
   cd Job_Search_AI_DJANGO
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv myapp
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     myapp\Scripts\activate
     ```
   - macOS / Linux:
     ```bash
     source myapp/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. Open **http://127.0.0.1:8000/** in your browser.

### (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

Then visit **http://127.0.0.1:8000/admin/**.

## Project Structure

```
Job_Search_AI_DJANGO/
├── manage.py
├── requirements.txt
├── [app_name]/
└── [project_name]/
```

## Author

**Neeraj Suhanda**
- GitHub: [@neeraj-2212](https://github.com/neeraj-2212)
- LinkedIn: [neeraj-suhanda](https://linkedin.com/in/neeraj-suhanda-48a1b4384/)

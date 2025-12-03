# Shorti.fy — URL Shortener (Django)

Shorti.fy is a simple and fast URL shortening service built with **Python + Django**.  
It allows users to create short, clean links and manage them in a personal dashboard.

---

## Preview

![Main Page](screenshots/png1.png)
![Main Page](screenshots/png2.png)


---

## Features

- Create short links from long URLs   
- Automatic short code generation  
- User authentication (sign up / log in)  
- User dashboard with all created links  
- Form validation & error handling  
- Clean minimalistic CSS interface  
- Instant redirection  

---

## Tech Stack

- **Python 3.x**  
- **Django 5.x**  
- HTML, CSS  
- SQLite (for development)  
- GitHub Desktop for version control  

---

## Project Structure
```
MainProject/

│── links/      # CRUD logic for short links
│── shortener/  # Project settings and configuration
│── templates/  # HTML templates
│── static/     # CSS, images
│── manage.py
│── .gitignore
```
---

## How to Run Locally

### 1. Clone the repository
```
git clone https://github.com/eva-maker/link-shortener.git
cd link-shortener
```
2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run migrations
```
python manage.py migrate
```
5. Start the development server
```
python manage.py runserver
```
Then open your browser at:
http://127.0.0.1:8000/

Example Shortened URLs
/abc123/ → https://www.youtube.com/....
/cat/    → https://docs.djangoproject.com/...

Future Improvements
- Click analytics
- Link logs and stats
- REST API version
- Dark mode

Author: Yeva Bykova
GitHub: https://github.com/eva-maker
Telegram: @evb_it

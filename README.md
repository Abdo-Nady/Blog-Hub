
# BlogHub

**BlogHub** is a Django-based blogging platform designed to help users explore, read, and share content effortlessly.  
It features a clean and responsive interface, dynamic context-driven templates, and essential pages like Home, Posts, About, and Contact.

---
## 🚧 Under Construction

This project is still a work in progress.  
New features, improvements, and fixes are being added regularly.

---

## 🚀 Features

- **Dynamic Home Page:** Shows featured topics, total posts, total authors, and spotlight content.
- **Posts Page:** Lists all blog posts with metadata (title, author, category, excerpt, published status, date).
- **About Page:** Presents company info, mission, values, and team size.
- **Contact Page:** Includes company contact info, departments, business hours, and social media links.
- **Responsive Design:** Built with Bootstrap 5 for smooth display on desktop and mobile.
- **Reusable Templates:** Context-driven Django templates for consistent UI.

---

## 📂 Project Structure

```

BlogHub/
│
├── blog/                  # Django app
│   ├── templates/blog/    # HTML templates: home.html, posts.html, about.html, contact.html
│   ├── views.py           # Views for handling pages and context
│   └── urls.py            # App URLs
│
├── static/                # Static files (Bootstrap JS, CSS)
│
├── BlogHub/               # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3             # SQLite database (default)
└── requirements.txt       # Project dependencies

````

---

## 🛠️ Tech Stack

- **Backend:** Django 5.2.8 (Python)
- **Frontend:** HTML, Bootstrap 5
- **Database:** SQLite (default)
- **Template Engine:** Django Templates

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/blog-hub.git
cd blog-hub
````

2. **Create and activate virtual environment**

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the development server**

```bash
python manage.py runserver
```

6. **Open in browser**

```
http://127.0.0.1:8000/
```
## ⚠ Disclaimer

This project is developed purely for *learning and educational purposes*.  
It is *not ready for production* and should not be used for commercial purposes.


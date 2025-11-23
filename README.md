# **BlogHub**

**BlogHub** is a Django-based blogging platform built to provide a clean, organized, and flexible reading and writing experience.
It includes full post management, user authentication, comments, advanced search, pagination, and personalized user pages.

---

## 🚀 **Features**

### 📝 **Blog & Post Management**

* Full **CRUD** for blog posts (Create, Read, Update, Delete).
* Proper rendering of post content with preserved line breaks.
* Arabic and English writing support.
* Dedicated user pages:

  * **My Posts**
  * **Drafts**

### 💬 **Comments System**

* Full comment functionality under each post.
* Each comment linked to its author and the post.
* Comment moderation available in Django Admin.

### 🔐 **Authentication (CBVs)**

* Login
* Register
* Logout
* Implemented using **Class-Based Views**.

### 🔍 **Advanced Search & Filtering**

* Search across:

  * Title
  * Excerpt
  * Category
  * Author
* Author filter
* Category filter
* Featured Posts section
* **Pagination** for:

  * Search results
  * Category pages

### 🏗️ **Architecture & Enhancements**

* Replaced all hardcoded data with PostgreSQL-backed models.
* Removed redundant and duplicated data.
* Template inheritance across all pages.
* Replaced hardcoded URLs with named URL tags.
* Cleaned up code for better maintainability.

### 🛠️ **Admin Improvements**

* Extended Django Admin with:

  * Categories
  * Posts
  * Comments
  * Tags
  * Blog metadata
* More organized layout and improved content management.

---

## 📄 **Pages**

* **Home** (Featured posts + statistics)
* **Posts List**
* **Post Detail** (with comments)
* **Categories Page**
* **Tags Page**
* **Search Results** (with pagination)
* **My Posts**
* **Drafts**
* **About**
* **Contact**
* **Login / Register / Logout**

---

## 📂 **Project Structure**

```
BlogHub/
│
├── blog/
│   ├── templates/blog/
│   │   ├── home.html
│   │   ├── posts.html
│   │   ├── post_detail.html
│   │   ├── categories.html
│   │   ├── search_results.html
│   │   ├── my_posts.html
│   │   ├── drafts.html
│   │   └── auth/ (login, register)
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
│
├── BlogHub/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
└── requirements.txt
```

---

## 🛠️ **Tech Stack**

* **Backend:** Django 5.2.8
* **Frontend:** HTML + Bootstrap 5
* **Database:** PostgreSQL
* **Template Engine:** Django Templates
* **Auth:** Django built-in authentication (CBVs)

---

## ⚙️ **Installation**

### 1. Clone the repository

```bash
git clone https://github.com/Abdo-Nady/Blog-Hub.git
cd Blog-Hub
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

* Create a PostgreSQL database and user, e.g.,

```sql
CREATE DATABASE bloghub;
CREATE USER bloguser WITH PASSWORD 'yourpassword';
ALTER ROLE bloguser SET client_encoding TO 'utf8';
ALTER ROLE bloguser SET default_transaction_isolation TO 'read committed';
ALTER ROLE bloguser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bloghub TO bloguser;
```

* Update `settings.py` DATABASES section accordingly:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bloghub',
        'USER': 'bloguser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the server

```bash
python manage.py runserver
```

### 7. Open in browser

```
http://127.0.0.1:8000/
```

---

## ⚠️ Disclaimer

This project is intended for **learning and educational purposes only**.
It is **not production-ready** and should not be used for commercial deployment.

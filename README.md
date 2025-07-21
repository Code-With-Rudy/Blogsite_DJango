# 📝 Personal Blog Site

A **Python-based personal blog website** built with the **Django** framework. This project enables users to create, edit, and publish blog posts with full **user authentication**, a clean Bootstrap-based UI, and a responsive design.

---

## 🔍 Features

### ✅ Blog Post Management (CRUD)
- **Create**: Authenticated users can add new blog posts.
- **Read**: All visitors can browse posts and view full details.
- **Update**: Authors can edit their own posts.
- **Delete**: Authors can delete their posts.

### 🔐 User Authentication
- **Registration**: New users can sign up.
- **Login/Logout**: Secure login/logout mechanisms.
- **Authorization**: Only authors can modify or delete their posts.

### ⚙️ Admin Interface
- Django's built-in admin panel for managing blog content and user accounts.

### 🎨 Responsive Design
- Clean and mobile-friendly layout using **Bootstrap 5**.

---

## 🧰 Technologies Used

- **Backend**: Python 3.x, Django 5.x
- **Database**: SQLite (development default)
- **Frontend**: HTML5, CSS3, Bootstrap 5, Django Templates (Jinja2)

---

## 🚀 Setup Instructions

### 🔧 Prerequisites
- Python 3.x installed
- `pip` (Python package installer)

### 📥 1. Clone the Repository

```bash
git clone (https://github.com/Code-With-Rudy/Blogsite_DJango)
cd blogproject
```
---
🛠️ 2. Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate it:

Windows: .\venv\Scripts\activate

macOS/Linux: source venv/bin/activate

📦 3. Install Dependencies
bash
Copy
Edit
pip install Django
# Or, if you have a requirements.txt:
pip install -r requirements.txt
🗃️ 4. Apply Database Migrations
bash
Copy
Edit
python manage.py makemigrations blog
python manage.py migrate
👤 5. Create Superuser
bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up your admin account.

📁 6. Static Files Directory
bash
Copy
Edit
mkdir static
▶️ 7. Run the Server
bash
Copy
Edit
python manage.py runserver
Visit: http://127.0.0.1:8000/

🌐 Usage
Home: http://127.0.0.1:8000/ – View all posts.

Admin Panel: http://127.0.0.1:8000/admin/

Login: http://127.0.0.1:8000/accounts/login/

Register: http://127.0.0.1:8000/register/

Create Post: http://127.0.0.1:8000/post/new/

Edit/Delete: Available only for authors on the post detail page.

📁 Project Structure
cpp
Copy
Edit
blogproject/
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   └── blog/
│   │       ├── post_list.html
│   │       ├── post_detail.html
│   │       └── post_form.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── myblogproject/
│   ├── settings.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── manage.py
└── db.sqlite3
🚧 Future Enhancements
✅ Comments System

✅ User Profile Pages

✅ Image Upload in Posts

✅ Rich Text Editor (WYSIWYG)

✅ Search Functionality

✅ Categories/Tags

✅ Pagination

✅ Live Deployment (Heroku, Render, etc.)

📄 License
This project is licensed under the MIT License.

sql
Copy
Edit
MIT License

Copyright (c) Rudranil Goswami GNIT

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...


🙌 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

📫 Contact
Feel free to connect with me on LinkedIn or email for any queries or collaborations!

vbnet
Copy
Edit

Let me know if you'd like a version with badges, screenshots, or deployment guides (e.g., for Render or 

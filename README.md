<div align="center">
  <h1>🌟 Hello Django Project 🌟</h1>
  <p>
	 <img src="https://img.shields.io/badge/Django-4.x-green?style=flat-square&logo=django" alt="Django">
	 <img src="https://img.shields.io/badge/Deployed-PythonAnywhere-blue?style=flat-square&logo=python" alt="PythonAnywhere">
  </p>
  <p>
	 <b>A simple, elegant Django web application with user authentication, contact form, and more.</b>
  </p>
</div>

---

## 🚀 Live Demo

👉 [Visit the deployed Hello Django project!](https://ibrahimsattar.pythonanywhere.com/)

---

## 📚 Project Overview

This is a Django-based web application featuring:

- User authentication (login, signup, logout)
- Contact form with database storage
- Informational pages (About, Pricing, etc.)
- Session-based user experience
- Responsive and clean UI (customizable with your own styles)

## 🗂️ Project Structure

```
Hello/
├── db.sqlite3
├── manage.py
├── Hello/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── home/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
├── static/
│   └── ...
└── templates/
	 ├── index.html
	 ├── about.html
	 ├── contact.html
	 └── ...
```

## ✨ Features

- Secure user authentication
- Contact form with success messages
- Session management
- Modular Django app structure
- Easy deployment on PythonAnywhere

## 🛠️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/your-django-repo.git
   cd Hello
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the app:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## 🌐 Deployment

This project is deployed on PythonAnywhere:

- [https://ibrahimsattar.pythonanywhere.com/](https://ibrahimsattar.pythonanywhere.com/)

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.

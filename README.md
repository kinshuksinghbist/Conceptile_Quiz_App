
# Quiz App

[Check it out Live](https://conceptile-quiz-app-i3kq.onrender.com/)
NOTE: 
USER: kinshuk
PASSWORD: a

A simple and elegant quiz application built using Django, Jinja templates, Tailwind CSS, and SQLite. This app allows users to answer questions and view their results in a clean, professional interface.


---

## 📋 Tech Stack

- **Backend**: [Django](https://www.djangoproject.com/)  
- **Templating**: [Jinja Templates](https://jinja.palletsprojects.com/) (built into Django)  
- **Frontend**: [Tailwind CSS](https://tailwindcss.com/)  
- **Database**: [SQLite](https://www.sqlite.org/)  

---

## 💡 Why This Tech Stack?

The choice for tailwindcss and sqlite db was made becuase they are fast and flexible. A SQLite DB doesnt require a server setup and tailwindcss is pug and play. 

---

## ⚙️ Setup Instructions

Follow these steps to set up the project locally:

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/kinshuksinghbist/Conceptile_Quiz_App.git
   cd quiz-app
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```
5. **Run the x.py script, if using new instance of DB or connceting another DB engine**  
  ```bash
   python manage.py x
   ```

---

## 🛠 Improvements Possible

1. **New User Generation**:  
   - While there is one superuser configured right now, enabling sign up funcitonality would be a big plus

2. **Changing the DB engine to something like POSTGRESQL for more robust scaling**:  
  
3. **Django could be configured with NextJS for more flexbility and better UI**:  

---

## 🎉 Conclusion

This **Quiz App** demonstrates a clean architecture with Django as the backend, Jinja templates for rendering, and Tailwind CSS for modern UI styling. SQLite ensures simplicity and ease of use during development.



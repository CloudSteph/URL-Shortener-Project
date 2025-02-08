# URL Shortener Project 🚀

This is a **simple URL shortner** built with Flask. It allows users to:
✅ Enter a **long URL**
✅ Generate a **short URL**
✅ Redirect users when they visit the short URL

## 📌 Features
- Shorten long URLs into unique short links
- Redirect users from short URLs to their original links.
- Uses SQLite for storing and retrieving shortened URLs.
- Minimal UI for easy interation

---

## 📁 Project Structure

url_shortener/ 
│── app.py # Flask (backend) 
│── venv/ # Virtual environment 
│── templates/ 
│ ├── index.html # HTML file for user input form (frontend)
│── README.md # Project documentation

---

## ⚙️ Setup Instructions

**1. Clone the Repository**

'''bash
$ git clone https://github.com/CloudSteph/URL-Shortener-Project.git

**2. Set Up a Virtual Environment**

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

**3. Install Dependencies**

Install Flask:
pip install flask

**4. Initialize the SQLite Database**

python initialize_db.py

**4. Run the Flask.app**
python app.py

## 🖥️ How to use the URL Shortener
1. Visit the provided site from your terminal in your browser
2. Enter a long URL and click **Shorten**
3. Click on the generated shortened url provided and that should redirect you to the original URL! 🎉

## 🛠️ Next Steps:
◆ Store shortened URLs in SQLite (so they don't disappear on the restart).
◆ Improve the UI with Bootstrap for better design.
◆ Deploy the app online so others can use it.

## 👩🏻‍💻 Author

Created by Stephanie Liew 🚀










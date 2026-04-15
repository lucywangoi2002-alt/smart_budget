# 💰 SmartBudget – Personal Finance Management System

SmartBudget is a modern web-based personal finance management application built with **Django** and **Bootstrap** that helps users track income, expenses, and spending categories while gaining intelligent insights into their financial habits.

The system provides a simple, clean, and interactive dashboard designed to promote better budgeting and financial decision-making.

---

## 🚀 Features

### 🔐 Authentication
- User registration and login system
- Secure authentication using Django Auth
- Toast notifications for user actions
- Password visibility toggle
- Form validation with disabled submit until valid

### 💵 Financial Management
- Add Income records
- Add Expense records
- Create and manage expense categories
- Organized financial tracking

### 📊 Smart Insights
- Category-based expense analysis
- Smart spending insights
- Visual reports using Chart.js
- Budget behavior monitoring

### 🎨 User Interface
- Responsive Bootstrap 5 design
- Modern navbar layout
- Toast notification system
- Clean login & signup UI
- Mobile-friendly interface

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** SQLite (default, configurable)
- **Charts:** Chart.js
- **Authentication:** Django Authentication System

---

## 📂 Project Structure
│
├── accounts/ # Authentication & user management
├── expenses/ # Expense tracking logic
├── income/ # Income management
├── templates/ # HTML templates
├── static/ # CSS, images, JS
└── manage.py


---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/smartbudget.git
cd smartbudget
```

 ## Create Virtual Environment
 ```
python -m venv venv
source venv/bin/activate
```

## Install requirements
```
pip install -r requirements.txt
```

## Create database
```
sudo -u postgres psql

CREATE database my_database_name;
```

### Note: Update the database information in the settings.
        - 'ENGINE': 'django.db.backends.postgresql',
        - 'NAME': .....,
        - 'USER': .....,
        - 'PASSWORD': .....,
        - 'HOST': .....,
        - 'PORT': .....,

## Run migrations
```
python manage.py migrate
```

## Start server
```
python manage.py runserver
```

### Open 
```
http://127.0.0.1:8000/
```

### 🎯 Future Improvements
AI-powered spending predictions
Monthly budget goals
Export reports (PDF/Excel)
REST API integration
Mobile app version

### 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

### MIT License

Copyright (c) 2026 Lucy Wangoi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

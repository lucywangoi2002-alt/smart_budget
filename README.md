# SmartBudget – Personal Finance Management System

SmartBudget is a modern web-based personal finance management application built with **Django** and **Bootstrap** that helps users track income, expenses, and spending categories while gaining intelligent insights into their financial habits.

The system provides a simple, clean, and interactive dashboard designed to promote better budgeting and financial decision-making.

---

## Features

### Authentication
- User registration and login system
- Secure authentication using Django Auth
- Toast notifications for user actions
- Password visibility toggle
- Form validation with disabled submit until valid

### Financial Management
- Add Income records
- Add Expense records
- Create and manage expense categories
- Organized financial tracking

### Smart Insights
- Category-based expense analysis
- Smart spending insights
- Visual reports using Chart.js
- Budget behavior monitoring

### User Interface
- Responsive Bootstrap 5 design
- Modern navbar layout
- Toast notification system
- Clean login & signup UI
- Mobile-friendly interface

---
## Screenshots

### Sign Up Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/b3609b21-7e3d-45a8-97b8-ba3621eea01b" />

### Login Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/59ab8037-b8c5-49c4-a435-cc0172b7cb76" />

### Dashboard Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/d08816bd-69e2-419e-92aa-15828e86a342" />

### Income List Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/e24b667c-b96c-4b77-b165-7a8d3feaf4c2" />

### Add Income Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/c97ac6e8-50e2-460e-9731-0b3ddeb5114c" />

### Expense list Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/95d8a5c4-a628-4841-b066-3c3f7bf45dc6" />

### Add Expense Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/a3df5f72-c229-492e-9508-860c300c5d03" />

### Category List Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/9ad7518b-10da-49fb-9583-45ebab9e15ba" />

### Add category Page

<img width="1866" height="964" alt="Image" src="https://github.com/user-attachments/assets/6e60f967-f9ec-43e1-a833-74df5e147d72" />

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** PostgrSQL
- **Charts:** Chart.js
- **Authentication:** Django Authentication System

---

---

## Installation

### Clone Repository

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
## Create .env file
```
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=your-database-name
DB_USER=your-userdb
DB_PASSWORD=your-bd-password
DB_HOST=localhost
DB_PORT=5432
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
EMAIL_HOST_USER=johndoe@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

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

### Future Improvements
AI-powered spending predictions
Monthly budget goals
Export reports (PDF/Excel)
REST API integration
Mobile app version

### Contributing

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




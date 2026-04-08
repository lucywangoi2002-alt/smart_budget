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

## Screenshots
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/7ab7c22b-9e40-48c4-abc6-6fa693738df5" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/ad4cffd5-823f-4f25-a089-28c2d0e8ebe0" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/f760115b-83fd-4072-8b43-ed16d6cfb462" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/f2bb4007-a7e7-4a48-8607-1a8b4aa627f8" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/db6fe83b-2ec0-40c8-9f78-731c9bfb6356" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/14436528-c7b6-487d-89ab-2c8157b55c78" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/6b355140-4079-4c3e-87a9-b69edc70a302" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/e7be3bb5-02ce-45dc-bb0d-ac3e284a034c" />
<img width="1857" height="928" alt="Image" src="https://github.com/user-attachments/assets/ddc3a575-5321-46a6-badf-adbb5308f86b" />


## 📂 Project Structure
```
│
├── accounts/ # Authentication & user management
├── expenses/ # Expense tracking logic
├── income/ # Income management
├── templates/ # HTML templates
├── static/ # CSS, images, JS
└── manage.py
```


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

### 📄 License

This project is licensed under the MIT License.

### 👨‍💻 Author

Lucy Waweru Wangoi
@2026

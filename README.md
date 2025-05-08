# 💸 Expense Tracker with Budget Alerts

A simple, lightweight Django web application to help you track daily expenses, manage a personal budget, and visualize spending—all without the need to sign up or log in.

---

## 🚀 Features

- ✅ Add, edit, and delete income and expense entries
- 📊 Visualize your spending with Chart.js pie charts
- ⚠️ Set a monthly budget and get an alert when expenses exceed it
- 💾 Export all your expense data to a CSV file
- 🔒 No sign-up required — session-based temporary storage
- 📱 Fully responsive and mobile-friendly interface using Bootstrap

---

## 📸 Screenshots

> Add screenshots here showing home page, expense form, budget alert, and chart.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Charts:** Chart.js (Pie chart for visualizing spending)
- **Storage:** Session-based (No database or login system)
- **Export:** CSV file generation using Python's `csv` module

---

## 🔔 Budget Alert Feature

The app allows users to set a budget for their spending. When expenses exceed this limit, a popup alert is triggered to inform the user.

### How it works:
- Budget is set using a form (`POST`)
- Expenses are stored in Django sessions
- When a new expense is added:
  - If total expenses exceed the budget, a Bootstrap modal or alert is triggered on the expense page

---

## 🧩 How It Works

1. Set your monthly budget
2. Add expenses (e.g., groceries, rent, travel)
3. View your total spend vs budget
4. Analyze spending via charts
5. Export your data as CSV
6. Clear session to start fresh

---

## 📂 Project Structure

expense-tracker/
│
├── tracker/ # Main Django app
│ ├── templates/tracker/ # HTML templates
│ │ ├── home.html
│ │ ├── expense.html
│ │ ├── viewExpense.html
│ │ ├── chart.html
│ │ └── about.html
│ ├── views.py # App logic (budget, expenses, alerts)
│ └── urls.py
│
├── static/ # Static files (CSS/JS)
├── manage.py
└── README.md


## 📝 Developer Info

👨‍💻 Developer: Nesh Sinha
🎓 Student at: B.Tech Computer Science
📬 Email: nsnesh25@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/nesh-sinha-36aa54270/
💻 GitHub: https://github.com/Nesh-Sinha


## 💡 Why I Built This

As a student learning Django and Python, I wanted to create something useful and relatable. Managing money is a challenge for many, and this app makes it easier without needing a full-fledged login system or database.
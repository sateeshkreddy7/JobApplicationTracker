# Job Application Tracker

\# Job Application Tracker



A Django-based web application for managing and tracking job applications in one place.



\## 📌 Project Overview



The Job Application Tracker helps users maintain their job application records and monitor their application progress.



Users can create an account, add job applications, update application details, search and filter applications, and track application statuses through a dashboard.



\## 🚀 Features



\- User Registration and Login

\- Secure User Authentication

\- Add Job Applications

\- Edit Application Details

\- Delete Applications

\- Search by Company or Job Title

\- Filter Applications by Status

\- Application Status Tracking

\- Dashboard Statistics

\- Interview Date Tracking

\- Salary Information

\- Job Link Storage

\- Notes for Each Application

\- Responsive Design



\## 📊 Application Status



The application supports the following statuses:



\- Applied

\- Shortlisted

\- Interview

\- Selected

\- Rejected



\## 🛠️ Technologies Used



\- Python

\- Django

\- HTML5

\- CSS3

\- SQLite

\- Git

\- GitHub



\## 📁 Project Structure



```text

JobApplicationTracker/

│

├── applications/

│   ├── migrations/

│   ├── static/

│   │   └── applications/

│   │       └── style.css

│   ├── templates/

│   │   └── applications/

│   │       ├── add\_application.html

│   │       ├── dashboard.html

│   │       ├── delete\_application.html

│   │       ├── edit\_application.html

│   │       ├── login.html

│   │       └── register.html

│   ├── forms.py

│   ├── models.py

│   ├── urls.py

│   └── views.py

│

├── jobtracker/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── manage.py

├── .gitignore

└── README.md


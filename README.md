Raspberry Pi - Attendance System
=============

Raspberry Pi attendance system based on QR code.

###scan.py

This file has all the back-end needed for capturing the picture to scanning and adding to database

It also controls the LEDs Red and Green

Red for some Error (Not blinking) and Active (Blinking)

Green for feedback as the QR code has been scanned

###Flask App:

This folder is the root for flask web app.

APP ROOT flask-app/
│   ├── forms.py		Forms
│   ├── \__init__.py		
│   ├── models.py		DB
│   ├── static
│   │   └── css			Skeleton Framwork CSS
│   │       ├── base.css
│   │       ├── layout.css
│   │       ├── main.css
│   │       └── skeleton.css
│   ├── templates		
│   │   ├── index.html		Base HTML Template
│   │   ├── register.html	Registration Form Template
│   │   └── thankyou.html	Response Thank you
│   └── views.py		
├── app.db			Generate this by running db_create.py
├── config.py			Config Variables like path and mail credentials
├── db_create.py
└── run.py			Final Script for running app.


# Django-Rest-Api

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?style=flat&logo=django)

This project is built using Django and Django Rest Framework (DRF) to provide a RESTful API for managing products, categories, and related functionality.

## Features
- Product and category management using Django models.
- RESTful API created with Django Rest Framework.
- Allows adding, updating, and retrieving products.

## Requirements
Before you start, make sure you have the following installed:

- Python 3.8+ (You can check your Python version by running `python --version` or `python3 --version`).
- Django 5.1.x (The version used in this project).
- Django Rest Framework.

You can install the required packages using `pip` and the `requirements.txt` file (see below).

## Installation

### 1. Clone the repository
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/EmmaHarutyunyan/Django-Rest-Api.git
```


### 2. Navigate to the project folder
After cloning, go into the project directory:

```bash
cd Django-Rest-Api
```

### 3. Set up a virtual environment
It is recommended to use a virtual environment for Python projects. If you don't have `virtualenv` installed, you can install it by running:

```bash
pip install virtualenv
```

Then, create and activate the virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```


### 4. Install requirements.txt


Install the required Python packages (including Django and Django Rest Framework) by running the following command:

```bash

pip install -r requirements.txt
```

### 5. Set up environment variables

Create a .env file in the root of your project and add the following environment variables:

```bash
SECRET_KEY=your_secret_key
```

### Structure of the project:

├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── myAPI/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── migrations/
│   └── urls.py
├── db.sqlite3
├── manage.py
├── .env
├── requirements.txt
└── README.md


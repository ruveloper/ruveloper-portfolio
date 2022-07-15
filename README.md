# 🐱‍💻 Portfolio project

[![GitHub](https://img.shields.io/github/license/ruveloper/django-portfolio-project)](https://www.mit.edu/~amini/LICENSE.md)

![Project preview](/media/default/porfolio_preview/home.jpg "Project preview")

### Build with:

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](http://www.djangoproject.com/)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindui.com/)

## Features:

- Production-ready
- Responsive design
- Glassmorphism style
- Fully customizable with Django Admin
- Component approach using Django Templates
- WYSIWYG editor to manage the project content
- Save record and send email on contact form success

** ✨ GETTING STARTED WITH DEV MODE**

1. Create a python virtualenv and activate


2. Install requirements:
   ```
   pip requirements -r ./requirements/local.txt
   ```

3. Init Django:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```


4. [Optional] Load default/test data:
   ```
   python manage.py loaddata default_data
   ```


4. Init Tailwind:
    - Rename .env-dev-template to .env and set the NPM_BIN_PATH
    - Install node modules

   ```
   python manage.py tailwind install
   ```

5. Run both tailwind and dev server on port:
   ```
   python manage.py runserver
   python manage.py tailwind start
   ```

6. Visit: http://127.0.0.1:8000/

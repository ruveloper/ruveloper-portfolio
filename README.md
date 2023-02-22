# 🐱‍💻 Ruveloper Portfolio

[![GitHub](https://img.shields.io/github/license/ruveloper/django-portfolio-project)](https://www.mit.edu/~amini/LICENSE.md)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Coverage Status](./media/default/coverage-badge.svg?dummy=8484744)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ruveloper/ruveloper-portfolio/main.svg)](https://results.pre-commit.ci/latest/github/ruveloper/ruveloper-portfolio/main)
[![Django CI](https://github.com/ruveloper/ruveloper-portfolio/actions/workflows/django_ci.yaml/badge.svg?branch=main)](https://github.com/ruveloper/ruveloper-portfolio/actions/workflows/django_ci.yaml)
[![Django CD](https://github.com/ruveloper/ruveloper-portfolio/actions/workflows/django_cd.yaml/badge.svg?branch=main)](https://github.com/ruveloper/ruveloper-portfolio/actions/workflows/django_cd.yaml)

![Home preview](/media/default/porfolio_preview/ruveloper-portfolio.jpg "Home preview")

# --> 👨‍💻 [Ruveloper Website](https://www.ruveloper.dev) 🌐 <--

### Personal portfolio based on [Django Portfolio Project](https://github.com/ruveloper/django-portfolio-project), visit the link above to see it in action.

### Build with:

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](http://www.djangoproject.com/)
[![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org/)
[![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://developer.mozilla.org/docs/Web/JavaScript)
[![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindui.com/)

## Features:

### Project-wide features

- Production-ready
- Scalable project structure
- CI/CD with GitHub Actions
- Internationalization (EN and ES)
- Component approach using Django Templates system
- Fully customizable with Django Admin
- WYSIWYG editor to manage the project content (TinyMCE)
- Save record and send email on contact form success
- Read-only REST API to extract information
- Static files compression and HTML minify
- reCaptcha v3 form validation

### Website features

- Responsive design
- Glassmorphism style
- Language selector
- Front-end cache and transitions with Barba.js and GSAP

## ✨ GETTING STARTED WITH DEV MODE

1. Create a python virtualenv and install requirements:
   ```
   python -m venv .venv
   (windows) .\.venv\Scripts\activate
   pip install -r .\requirements\local.txt
   ```

2. Set the environment variables:
    - Copy or rename **.env-dev-template** to **.env**
    - Set the NPM_BIN_PATH variable


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

5. Run both tailwind and dev server:
   ```
   python manage.py tailwind start
   python manage.py runserver
   ```

6. Visit: http://127.0.0.1:8000/

7. Change: http://127.0.0.1:8000/admin/

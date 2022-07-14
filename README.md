# Django + Tailwind - Portfolio project

---
License: **MIT**


Portfolio project with:
- Python-Django
- Tailwind
- Browser Reload
- Glassmorphism design style
- Component approach using Django Templates

**GETTING STARTED WITH DEV MODE**

1. Create a python virtualenv and activate


2. Install requirements

   `pip requirements -r ./requirements/local.txt`


3. Init Django

   `python manage.py makemigrations`

   `python manage.py migrate`

   `python manage.py createsuperuser`


4. Init Tailwind
   - Rename .env-dev-template to .env and set the NPM_BIN_PATH
   - Install node modules

   `python manage.py tailwind install`


5. Run tailwind and dev server on port 8000

   `python manage.py runserver`

   `python manage.py tailwind start`


6. Visit: http://127.0.0.1:8000/

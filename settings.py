settings.py
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install django djangorestframework
django-admin startproject gas_utility
cd gas_utility
python manage.py startapp customer_service

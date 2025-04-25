cd ..

call venv/Scripts/activate.bat

set DJANGO_SETTINGS_MODULE=server.settings.development

python manage.py runserver 0.0.0.0:8200
#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
from decouple import config
import os
import sys

# Загружаем секретный ключ из .env
SECRET_KEY = config('SECRET_KEY')

# Загружаем режим отладки
DEBUG = config('DEBUG', default=True, cast=lambda x: x == 'TRUE')

# Настройки базы данных (если используешь PostgreSQL или другую СУБД)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # или 'django.db.backends.sqlite3'
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': 'localhost',  # Для PostgreSQL или MySQL
        'PORT': '5432',  # Порт базы данных
    }
}

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xsenia_kriProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

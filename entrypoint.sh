#!/bin/sh
set -e

echo "=== Запуск миграций ==="
python manage.py migrate --noinput

echo "=== Статики ==="
python manage.py collectstatic --noinput


echo "=== Запуск сервера ==="
gunicorn core.wsgi:application --bind 0.0.0.0:8001 --workers 3
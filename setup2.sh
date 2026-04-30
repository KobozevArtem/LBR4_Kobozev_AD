#!/bin/bash
echo "Запуск развертывания Django-приложения..."
# Обновление pip
echo "Обновление pip..."
python -m pip install --upgrade pip
# Установка зависимостей
echo "Установка зависимостей..."
pip install django numpy pandas matplotlib
# Применение миграций
echo "🗄 Применение миграций..."
python manage.py migrate
# Сбор статики (необязательно, но правильно)
echo "Сбор статических файлов..."
python manage.py collectstatic --noinput
# Запуск сервера
echo "Запуск сервера..."
python manage.py runserver 0.0.0.0:3000
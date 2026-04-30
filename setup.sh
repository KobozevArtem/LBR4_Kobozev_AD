#!/bin/bash
pip install django
python manage.py migrate
echo "Setup completed successfully!"

# Hacker-news-Task
python manage.py runserver
celery -A config worker --loglevel=INFO --concurrency 1 -P solo
celery -A config worker --loglevel=info
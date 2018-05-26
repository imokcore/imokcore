release: ./release-tasks.sh
schedule: python schedule.py
web: gunicorn project.wsgi --name im-ok-core-service --workers 3 --access-logfile "-" --error-logfile "-"
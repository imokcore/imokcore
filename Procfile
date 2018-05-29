release: ./release-tasks.sh
clock: python clock.py
web: gunicorn project.wsgi --name im-ok-core-service --workers 3 --access-logfile "-" --error-logfile "-"
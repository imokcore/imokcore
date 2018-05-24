#!/usr/local/bin/dumb-init /bin/sh

echo "Running in prod"
export DJANGO_SETTINGS_MODULE='project.settings.prod'


#if [ "$STARBUG_CLUSTER" = 'eu-production' -o "$STARBUG_CLUSTER" = 'eu-staging' ]; then
#    echo "Running in prod"
#    export DJANGO_SETTINGS_MODULE='project.settings.prod'
#
#else
#    echo "Running in dev"
#    export DJANGO_SETTINGS_MODULE='project.settings.dev'
#fi

python manage.py migrate
python manage.py collectstatic --clear --noinput
python manage.py collectstatic --noinput

echo Creating users
python create_user.py

echo Starting Gunicorn.
gunicorn project.wsgi --name im-ok-core-service --workers 3 --access-logfile "-" --error-logfile "-"

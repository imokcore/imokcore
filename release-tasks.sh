#!/usr/bin/env bash

echp Migrate
python manage.py migrate

echo Creating users
python create_user.py
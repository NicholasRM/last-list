#!/bin/bash
set -o errexit
pip install -r requirements.txt
python ./lastlist/manage.py collectstatic --no-input
python ./lastlist/manage.py migrate

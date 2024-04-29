#!bin/bash
set -o errexit
pip install -r requirements.txt
python ./lastlist/manage.py collectstatic
python ./lastlist/manage.py migrate

#!/bin/bash

python3 -m venv /tmp/flask-venv
source /tmp/flask-venv/bin/activate

pip install flask
python3 server.py



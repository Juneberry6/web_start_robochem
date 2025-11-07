#!/bin/bash

cd /home/aermakov/github/ros2_rc5_control_pregrasp
source control_pregrasp/bin/activate
source setup_venv_and_build.sh

python3 /home/aermakov/github/tests_api/7_pos.py


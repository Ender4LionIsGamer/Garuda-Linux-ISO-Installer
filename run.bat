@echo off
title Installing requirements...
color 0b
echo [*] Running..
pip3 install -r requirements.txt
echo [*] Done!
title Running...
python3 main.py
exit

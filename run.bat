@echo off
call cmd
title Installing requirements...
color 0b
echo [*] Running..
pip3 install -r requirements.txt
echo [*] Done!
python3 main.py
exit

@echo off
pip install -r requirements.txt
pyinstaller test.spec
pause
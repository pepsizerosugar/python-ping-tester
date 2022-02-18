@echo off
pyinstaller --onefile --noconsole --icon=resource\img\icon.ico --name=PingPong Main.py
pause
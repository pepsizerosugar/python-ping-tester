@echo off
pyinstaller -F -w -i resource\img\icon.ico --add-data="resource/img/icon.ico;resource/img" -n PingPong Main.py
copy server_list.json dist
pause
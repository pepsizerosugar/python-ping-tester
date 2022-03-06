@echo off
pyinstaller -F -w -i Resource\img\icon.ico --add-data="Resource/img/icon.ico;resource/img" -n PingPong Main.py
set dir=dist\Resource\Server
if not exist %dir% mkdir %dir%
copy Resource\Server\server_list.json %dir%
pause
@echo off
pyinstaller -F -w -i Resource\Img\icon.ico --add-data="Resource/Img/icon.ico;Resource/Img" -n PingPong Main.py
set dir=dist\Resource\Server
if not exist %dir% mkdir %dir%
copy Resource\Server\server_list.json %dir%
pause
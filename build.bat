@echo off
pyinstaller -F -w -i Resource\img\icon.ico --add-data="Resource/img/icon.ico;resource/img" -n PingPong Main.py
mkdir dist\Resource\Server
copy Resource\Server\server_list.json dist\Resource\Server
pause
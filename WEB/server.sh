#!/bin/bash
SERVICE="webserver.py"
if ps -ef | grep $SERVICE | grep -v grep >/dev/null
then
    echo "$SERVICE is running"
else
    echo "$SERVICE stopped, restarting"
    python WEB/webserver.py 2> WEB/logfile.txt &
fi

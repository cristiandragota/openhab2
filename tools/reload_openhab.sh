#!/bin/bash
echo 'Start of the script'
cd /usr/local/projects
pwd
sudo git pull origin master
echo 'Loading the configuration done'
sudo service openhab2 restart
echo 'Server restart completed, waiting log for errors'
sleep 15s
tail -n 50 /var/log/openhab2/openhab.log | grep 'ERROR'

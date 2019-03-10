#!/bin/bash
echo 'Start of the script'
cd ~/openhab2
sudo git pull origin master
echo 'Loading the configuration done'
sleep 2s
echo 'Below changes reloaded by server'
tail -n 10 /var/log/openhab2/openhab.log | grep 'INFO'

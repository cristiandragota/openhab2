echo -e "Status of the services for IoT platform: \n"
echo " MQTT  broker server:"
sudo service mosquitto status | grep 'Active'
echo "----------------------------------"
echo " Database status:"
sudo systemctl status mysqld | grep 'Active'
echo "----------------------------------"
echo " Openhab2 server status:"
sudo service openhab2 status | grep 'Active'
echo "----------------------------------"

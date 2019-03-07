echo "Cleaning the local configuration from /etc/openhab2/......"
sudo rm -rf /etc/openhab2/*
time 5
echo "Adding the links to configuration files from current directory:" $PWD
sudo ln -s $PWD/rules /etc/openhab2/rules
sudo ln -s $PWD/items /etc/openhab2/items
sudo ln -s $PWD/persistence /etc/openhab2/persistence
sudo ln -s $PWD/scripts /etc/openhab2/scripts
sudo ln -s $PWD/services /etc/openhab2/services
sudo ln -s $PWD/sitemaps /etc/openhab2/sitemaps
sudo ln -s $PWD/things /etc/openhab2/things
sudo ln -s $PWD/html /etc/openhab2/html
sudo ln -s $PWD/sounds /etc/openhab2/sounds
sudo ln -s $PWD/transform /etc/openhab2/transform
sudo ln -s $PWD/icons /etc/openhab2/icons
echo " done/......"
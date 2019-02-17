cd /usr/local/projects
sudo git pull local master
echo 'Configuration reloaded'
sudo service openhab2 restart
echo 'Server reload completed'
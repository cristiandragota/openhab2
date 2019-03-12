#!/bin/bash  
sudo git add .  
read -p "Commit description: " desc  
sudo git commit -m $desc  
sudo git push origin master

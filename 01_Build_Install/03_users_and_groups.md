# Users and Groups

## Changing User Name
First you must create a different temporary user with sudo privliges so that you can change the other user's name.  
```bash
sudo adduser tempuser  # Create a new user
sudo usermod -aG sudo tempuser # Add tempuser to sudo group.
reboot # Log in as tempuser
grep 'sudo' /etc/group # Check that tempuser was added to sudo group
# -l change login name, -d set new home dir path, -m move old home dir to new one
sudo usermod -l new_username -d /home/new_username -m old_username 
sudo groupmod -n new_username  old_username # Change group name for new user
reboot
```

## Changing Password and Deleting Users
Can be done through the GUI  
Settings > System > Users   
Through the command line:  
```bash
sudo passwd [username] # Change user name
sudo deluser [username] # Delete user
```

## Change Hostname
```bash
sudo hostnamectl set-hostname [new_hostname]
sudo nano /etc/hosts # Change the hostname here: 127.0.1.1[new_hostname]
reboot
```
sudo groupadd gpio
sudo usermod -a -G gpio dongrow
sudo grep gpio /etc/group
sudo chown root.gpio /dev/gpiomem
sudo chmod g+rw /dev/gpiomem


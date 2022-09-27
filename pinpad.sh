#!/bin/bash
clear
echo 0 > /sys/bus/usb/devices/usb1/bConfigurationValue
echo "Reiniciando Pinpad ..."	
sleep 1
clear
echo "9"
sleep 1
clear
echo "8"
sleep 1
clear
echo "7"
sleep 1
clear
echo "6"
sleep 1
clear
echo "5"
sleep 1
clear
echo "4"
sleep 1
clear
echo "3"
sleep 1
clear
echo "2"
sleep 1
clear
echo "1"
sleep 1
echo 1 > /sys/bus/usb/devices/usb1/bConfigurationValue
clear
echo "Pinpad reiniciado!"	
sleep 2
clear
chmod 777 /dev/ttyACM0
/opt/pdv/configsLinux/config_perifericos
clear
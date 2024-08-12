#!/bin/bash
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

YELLOW=$(tput setaf 11)
RED=$(tput setaf 1)
WHITE=$(tput setaf 15)
BLUE=$(tput setaf 6)
GREEN=$(tput setaf 2)

function Banner {
	banner=$(<"Banner/Banner.txt")
	printf "${BLUE}$banner"
}

function Packet-Installer {
	printf "${GREEN}\n[+]${WHITE}Installing Packets..."
	sudo apt-get install qpdf -y &> /dev/null |
	sudo apt-get install git -y &> /dev/null |
	sudo apt-get install python3 -y &> /dev/null |
	sudo apt-get install p7zip-full -y &> /dev/null |
    sudo apt-get install python3-pip -y &> /dev/null |
    sudo apt-get install unrar -y &> /dev/null |
    sudo apt-get install rar -y &> /dev/null |
	sudo apt-get install tor -y &> /dev/null |
	printf "${GREEN}\n\n[+]${WHITE}Packets Installed"
	sleep 5
}

function Configuration {
	cd Configuration
	echo ";CHANGE THESE VALUE IF YOU WANT TO UPDATE YOUR SETTINGS FROM HERE">Configuration.ini
	echo ";BUT DO NOT CHANGE THE PARAMETERS NAME">>Configuration.ini
	echo "">>Configuration.ini		
	echo "[Settings]">>Configuration.ini
	echo "USERAGENT_PATH = Useragent/List.txt">>Configuration.ini
	echo "TOR_PROXY = False">>Configuration.ini
	echo "USERAGENT_CHANGE = False">>Configuration.ini
	echo "BREAK_TIME = 5">>Configuration.ini
	printf "${BLUE}\n[I]${WHITE}Default Configurations:\n"
	printf "${GREEN}\n[+]${WHITE}USERAGENT_PATH = ${GREEN}Useragent/List.txt"
	printf "${GREEN}\n[+]${WHITE}TOR_PROXY = ${GREEN}False"
	printf "${GREEN}\n[+]${WHITE}USERAGENT_CHANGE = ${GREEN}False"
	printf "${GREEN}\n[+]${WHITE}BREAK_TIME = ${GREEN}5"
	printf "${BLUE}\n\n[I]${WHITE}Configuration File: Configuration/Configuration.ini"
}

function installer {
	cd Passwords
	cd Default
	rm Untitled.txt &> /dev/null |
	cd ../
	cd ../
	cd ../
    printf "${BLUE}\n\n[I]${WHITE}Installing Himitsu\n"
	sleep 5
    Packet-Installer
	pwd
	Configuration
	sleep 5
	printf "${YELLOW}\n\n[v]${WHITE}Himitsu Installed Successfully\n\n"
    exit 1
}

if [ $(id -u) -ne 0 ];
	then
	clear
    Banner
	printf "${RED}\n\n[!]${WHITE}This Installer should be run as root try to execute the program with sudo\n\n"
	exit 1
fi
clear
Banner
installer 

# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Colors
from Core.Attacks import Cracker
from Core.Attacks import Xss
from Core.Common import Clear
from Core import Banner

class Display:
    
    @staticmethod
    def Choices():
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Insert a choice")
        choice = int(input("\n(1)Password-Cracker\t\t\t(2)File-Cracker\n(3)Online-Password-Cracker\t\t(4)XSS-Checker\n(5)Exit" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        if choice == 1:
            Cracker.Local.Password()
        elif choice == 2:
            Cracker.Local.File()
        elif choice == 3:
            Cracker.Online.Password()
        elif choice == 4:
            Xss.Test.Start()
        if choice == 5:
            exit()
    
    @staticmethod
    def Main():
        try:
            Clear.Screen.Clear()
            Banner.Picker.Get()
            Display.Choices()
        except KeyboardInterrupt:
            print(Colors.Color.WHITE + "\n\nExit Program")
            exit(1)

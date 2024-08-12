# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from time import sleep
from Core import Colors

class Picker:
    
    @staticmethod
    def Get():
        folder = "Banner"
        choice = "Banner.txt"
        f = open(folder + "/" + choice, "r", newline=None)
        for line in f:
            sleep(0.3)
            print(Colors.Color.BLUE + line.replace("\n", ""))
        f.close()
        print(Colors.Color.WHITE + "\nA Simple Red Team tool" + Colors.Color.BANNER + "\t\tCoded by Lucksi" + Colors.Color.RESET)
        print(Colors.Color.BLUE + "_________________________________________________")
        print(Colors.Color.BLUE + "|" + Colors.Color.WHITE + " Instagram:lucks_022" +
                Colors.Color.BLUE + "                           |")
        print(Colors.Color.BLUE + "|" + Colors.Color.WHITE + " Email:lukege287@gmail.com" +
                Colors.Color.BLUE + "                     |")
        print(Colors.Color.BLUE + "|" + Colors.Color.WHITE + " GitHub:Lucksi" +
                Colors.Color.BLUE + "                                 |")
        print(Colors.Color.BLUE + "|" + Colors.Color.WHITE + " Twitter:@Lucksi_22" +
                Colors.Color.BLUE + "                            |")
        print(Colors.Color.BLUE + "|" + Colors.Color.WHITE +
                " Linkedin:https://www.linkedin.com/in/lucksi" + Colors.Color.BLUE + "   |")
        print(Colors.Color.BLUE + "-------------------------------------------------")
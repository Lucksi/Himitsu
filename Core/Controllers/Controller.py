# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core import Colors
from Core import Menu

class Size:
    
    @staticmethod
    def Folder(name):
        count = 0
        for file in os.listdir(name):
            if file.endswith(".txt"):
                count = count + 1
        if count > 0:
            pass
        else:
            print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "No text file found in the {} folder".format(name))
            inp = input("Press enter to continue...")
            Menu.Display.Main()

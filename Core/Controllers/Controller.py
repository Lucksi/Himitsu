# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core import Colors
from Core import Menu

class Size:
    
    @staticmethod
    def Folder(name,type):
        count = 0
        if type == "Pwd":
            error = "Wordlist found (accepted only .txt files)"
            for file in os.listdir(name):
                if file.endswith(".txt"):
                    count = count + 1
        else:
            error = "Archive/File found (accepted only .zip,.rar,.7z and .pdf files)"
            for file in os.listdir(name):
                if file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".pdf"):
                    count = count + 1
        if count > 0:
            pass
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "No {} found in the {} folder\n".format(error,Colors.Color.GREEN + name + Colors.Color.WHITE))
            inp = input("Press enter to continue...")
            Menu.Display.Main()
# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
from Core import Colors
from Core import Menu
from time import sleep

class Size:
    
    @staticmethod
    def Wordlist(name,lists):
        count = 0
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Checking valide wordlist...\n")
        sleep(3)
        error = "Wordlist found or the only Wordlist found is an empty file (accepted only .txt files)"
        for file in os.listdir(name):
            if file.endswith(".txt"):
                count1 = 0
                filename = "Passwords/Default/" + file
                f = open(filename,"r",newline=None)
                reader = f.readlines()
                for line in reader:
                    count1 = count1 +1
                if count1 > 0:
                    lists.append(file)
                    valid = Colors.Color.GREEN + "True"
                else:
                    valid = Colors.Color.RED + "False"
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Filename:{} {}".format(file,valid))
        if len(lists) > 0:
            count = 1
            pass
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "No {} in the {} folder\n".format(error,Colors.Color.GREEN + name + Colors.Color.WHITE))
            inp = input("Press enter to continue...")
            #Menu.Display.Main()
        return count

    @staticmethod
    def Files(name):
        count = 0
        error = "Archive/File found (accepted only .zip,.rar,.7z and .pdf files)"
        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Checking files...\n")
        for file in os.listdir(name):
            if file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".pdf"):
                count = count + 1
                size = os.stat("Files/" + file)
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Filename:{} {} bytes".format(file,Colors.Color.GREEN + str(size.st_size) + Colors.Color.WHITE))
        if count > 0:
            pass
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "No {} in the {} folder\n".format(error,Colors.Color.GREEN + name + Colors.Color.WHITE))
            inp = input("Press enter to continue...")
        return count
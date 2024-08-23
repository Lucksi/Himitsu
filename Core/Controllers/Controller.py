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
        names = []
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
                    names.append(file)
                    valid = Colors.Color.GREEN + "True"
                else:
                    valid = Colors.Color.RED + "False"
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Filename:{} {}".format(file,valid))
        
        if len(names) > 0:
            if len(names) > 1:
                list_choice = int(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Do you want to use all the wordlists found?(1)Yes(2)No" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                if list_choice == 1:
                    for element in names:
                        lists.append(element)
                else:
                    count_files = 0
                    file_num = len(names)
                    while count_files < file_num:
                        pwd_file = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the wordlist file 'Insert Stop to finish'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        while pwd_file == "":
                            pwd_file = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the wordlist file 'Insert Stop to finish'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        if pwd_file in names:
                            if pwd_file not in lists:
                                print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Wordlist: {} added".format(Colors.Color.GREEN + pwd_file + Colors.Color.WHITE))
                                lists.append(pwd_file)
                                count_files = count_files + 1
                            else:
                                print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Wordlist: {} already inserted".format(Colors.Color.GREEN + pwd_file + Colors.Color.WHITE))
                        elif pwd_file == "Stop":
                            if len(lists) > 0:
                                count_files = file_num + 1
                            else:
                                print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Insert at least one wordlist file")
                        else:
                            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Insert one of the following wordlist file\n")
                            for element in names:
                                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + element)
            else:
                lists = names
            count = 1
            pass
        else:
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "No {} in the {} folder\n".format(error,Colors.Color.GREEN + name + Colors.Color.WHITE))
            inp = input("Press enter to continue...")
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
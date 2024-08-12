# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import random
from Core.Common import Settings

class Select:

    USERAGENTFILE = Settings.Get.Value("USERAGENT_PATH")
        
    @staticmethod
    def Useragent():
        f = open(Select.USERAGENTFILE, "r")
        value = f.readlines()
        current = ""
        agent = random.choice(value).replace("\n","")
        while current == agent:
            agent = random.choice(value).replace("\n","")
        current = agent
        f.close()
        return current
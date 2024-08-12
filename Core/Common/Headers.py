# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class Get:
   
    @staticmethod
    def Agent(mode,agent):
        if mode == 1:
            headers = {
                'User-Agent':'{}'.format(agent).replace("\n","") 
            }
        else:
            headers = {
                'User-Agent':'{}'.format(agent).replace("\n","") 
            }
        return headers
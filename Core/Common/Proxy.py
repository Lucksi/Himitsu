# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0


import json
import requests
from Core.Common import Settings
from Core import Colors

class Select:

    TOR_PROXY = Settings.Get.Value("TOR_PROXY")
        
    @staticmethod
    def Proxy():
        if Select.TOR_PROXY == "True" or Select.TOR_PROXY == True:
            final_proxis = {
                "http": "socks5h://127.0.0.1:9050",
                "https": "socks5h://127.0.0.1:9050"
            }
            ipUrl = "http://ip-api.com/json"
            ipReq = requests.get(ipUrl, proxies=final_proxis, timeout=15)
            reader = ipReq.text
            converted = json.loads(reader)
            ip = converted["query"]
            current = ip
            print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Test on your local network may not work with Tor Proxy")
        else:
            final_proxis = None
            current = "None"
        return current,final_proxis
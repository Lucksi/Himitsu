# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import requests
from Core.Common import Headers
from Core.Common import Useragent
from Core.Common import Settings
from Core.Common import Proxy
from Core import Colors
from time import sleep

class Create:

    CHANGING_AGENT = Settings.Get.Value("USERAGENT_CHANGE")
    BREAK_TIME = Settings.Get.Value("BREAK_TIME")
    
    @staticmethod
    def Send(url,typology,data,errortype,headers,payload,await_t,agent):
        proxy = Proxy.Select.Proxy()[1]
        change = int(Create.BREAK_TIME)
        if Create.CHANGING_AGENT == "True" or Create.CHANGING_AGENT == True:
            if await_t == change:
                sleep(1)
                print(Colors.Color.RED + "\n\n[-]" + Colors.Color.WHITE + "Changing Useragent: {}".format(Colors.Color.GREEN + agent))
                agent = Useragent.Select.Useragent()
                headers = Headers.Get.Agent(1,agent)
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Current Useragent: {}\n".format(Colors.Color.GREEN + agent))
                await_t = 0
        if typology == "POST":
            req = requests.post(url=url,data=data,allow_redirects=True,headers=headers,proxies=proxy)
        elif typology == "GET":
            req = requests.get(url=url,allow_redirects=True,headers=headers,proxies=proxy)
        if errortype == "status-code":
            if req.status_code == 200:
                response = "OK"
            else:
                response = "BAD"
        elif errortype == "Message-XSS":
            encod_payload = bytes(payload,"utf-8")
            if encod_payload in req.content or payload in req.content:
                response = "OK"
            else:
                response = "BAD"
        return response, req.content
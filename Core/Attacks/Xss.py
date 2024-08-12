# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0


from Core.Common import Request 
from Core import Colors
from Core.Common import Forms
from Core.Common import Headers
from Core.Common import Useragent
from Core.Common import Proxy
from tqdm import tqdm

class Test:

    @staticmethod
    def Send_payload(string,typologi,data,headers,payload,agent,report):
        with tqdm(total=1, initial=0, desc="Injecting payload") as bar:
            req = Request.Create.Send(string,typologi,data,"Message-XSS",headers,payload,0,agent)
            bar.update()
        if req[0] == "OK":
            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Payload injected Site vulnerable to XSS")
            vulnerable = "Vulnerable to xss: {}".format(payload)
        else:
            print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Site not vulnerable to XSS")
            vulnerable = "Not vulnerable to xss: {}".format(payload)
        f = open(report,"a")
        f.write("{}".format(vulnerable))
        f.close()
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Output: {}".format(Colors.Color.GREEN + str(req[1])))

    @staticmethod
    def Start():
        reportname = substring = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert filename for the output ex 'Example.txt'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        while reportname == "" or reportname.endswith("/") or ".txt" not in reportname:
            reportname = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert filename for the output ex 'Example.txt'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        report = "output/Web/Xss/{}".format(reportname)
        agent = Useragent.Select.Useragent()
        proxy = Proxy.Select.Proxy()
        headers = Headers.Get.Agent(1,agent)
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Initial Useragent: {}".format(Colors.Color.GREEN + agent))
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Tor Proxy Ip: {}".format(Colors.Color.GREEN + proxy[0]))
        auto = int(input(Colors.Color.BLUE + "\n[?]" + Colors.Color.WHITE + "Do you want to automatize the form recognizion process 'Works better on login pages'?(1)Yes(2)No" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->")) 
        if auto == 1:
            substring = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            while substring == "" or substring.endswith("/"):
                substring = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            substring2 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the rest of the url ex '/something.php' you can leave it empty and press enter if there is no further url part" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            if substring2 == "":
                string = substring
            else:
                string = substring + substring2
            print(Colors.Color.GREEN)
            with tqdm(total=1, initial=0, desc="Connecting") as bar:
                req = Request.Create.Send(string,"GET","","status-code",headers,"",0,agent)
                bar.update()
            parms = Forms.Get.Http_form(req[1],substring)
            contin = True
        else:
            string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            while string == "":
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            contin = True
            parms = ""
        f = open(report,"w")
        f.write("Website: {}\n\n".format(string))
        f.close()
        if contin:
            if parms != []:
                string = parms[1]
                reqt = parms[0]
                reqtype1 = len(parms)
                num = reqtype1 -2
            if parms == [] and auto == 1 or string == "Not-Located":
                if string == "Not-Located":
                    print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Cannot retrieve request url")
                else:
                    print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Something Went Wrong During the automatic scan")
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string == "":
                    string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                num = 0
                parms = "Undefined"
            elif parms == []:
                num = 0
                parms = "Undefined"
            elif string == "Not-Located":
                print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Cannot retrieve request url")
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string == "":
                    string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
            print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Request url: {}".format(Colors.Color.GREEN + string))
            if parms == "" or parms == "Undefined":
                reqtype = int(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the request method:\n(1)GET\t\t(2)POST" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string == "":
                    reqtype = int(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the request method:\n(1)GET\t\t(2)POST" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                if reqtype == 1:
                    reqt = "GET"
                elif reqtype == 2:
                    reqt = "POST"
            if reqt == "POST" or reqt == "Post" or reqt == "post":
                    if num == 0:
                        num = int(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert parameters number" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                    i = 0
                    data = {}
                    for i in range(1):
                        string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the parameter name and XSS payload ex 'Username = <script>alert('hello world')</script>'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        while string10 == "":
                            string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the parameter name and XSS payload ex 'Username = <script>alert('hello world')</script>'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        parameter = string10.split(" = ",1)[0].replace(" ","")
                        values2 = string10.rsplit(" = ",1)[1].replace(" ","").replace(parameter,"")
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "{}: {}".format(parameter,Colors.Color.GREEN + values2))
                        data.update({parameter:values2})
                        typologi = "POST"
            elif reqt == "GET" or reqt == "Get" or reqt == "get":
                string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the complete payload ex 'username=<script>alert('test');</script>'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string10 == "":
                    string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the complete payload ex 'username =<script>alert('test');</script>'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                values2 = string10.rsplit("=",1)[1].replace(" ","")
                string = string + "?" + string10.replace(" ","&")
                typologi = "GET"
                data = {}
            print(Colors.Color.GREEN)
            Test.Send_payload(string,typologi,data,headers,values2,agent,report)
            print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Result saved in: {}".format(Colors.Color.GREEN + report))
        inp = input(Colors.Color.WHITE + "\nPress enter to continue")
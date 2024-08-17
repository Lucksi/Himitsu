# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Colors
from time import sleep
from Core.Common import Request
from Core.Common import Forms
from Core.Passwords import Hashing
from Core.Common import Headers
from Core.Common import Useragent
from Core.Common import Proxy
from Core.Controllers import Controller
import base64
import os
from tqdm import tqdm


class Local:
    
    @staticmethod
    def base64_decode(string,type):
        encodedpwd = string.encode("utf-8")
        if type == "base64":
            try:
                base64_Byte = base64.b64decode(encodedpwd)
                finalpwd = base64_Byte.decode("utf-8")
            except Exception as e:
                print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Something went wrong Trying with BASE32 Decoding")
                sleep(2)
                try:
                    base64_Byte = base64.b32decode(encodedpwd)
                    finalpwd = base64_Byte.decode("utf-8")
                except Exception as e:
                    print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Something went wrong")
                    finalpwd = ""
        elif type == "base32":
            try:
                base64_Byte = base64.b32decode(encodedpwd)
                finalpwd = base64_Byte.decode("utf-8")
            except Exception as e:
                print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Something went wrong Trying with BASE64 Decoding")
                sleep(2)
                try:
                    base64_Byte = base64.b64decode(encodedpwd)
                    finalpwd = base64_Byte.decode("utf-8")
                except Exception as e:
                    print(Colors.Color.RED + "[-]" + Colors.Color.WHITE + "Something went wrong")
                    finalpwd = ""
        print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Decoded Password: {}".format(Colors.Color.GREEN + finalpwd))
        return finalpwd
    
    @staticmethod
    def Password():
        filesfolder = "Passwords/Default/"
        found = False
        attempt = 0
        file_names = []
        #Controller.Size.Folder(filesfolder,"Pwd",file_names)
        string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the password" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        foundpass = "" 
        while string == "":
            string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the password" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Input password: {}".format(Colors.Color.GREEN + string))
        type = Hashing.Get.Type(string)
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Algorithm type: {}".format(Colors.Color.GREEN + type))
        if type == "Common" or type == "Unknown":
            pass
        else:
            report = "output/Passwords/{}.txt".format(string)
            f = open(report,"w")
            f.write("Input Password: {}\n\n".format(string))
            f.close()
            if type == "base64" or type == "base32":
                foundpass = Local.base64_decode(string,type)
            else:
                Controller.Size.Folder(filesfolder,"Pwd",file_names)
                if found == False:
                    for name in file_names:
                        completefile = filesfolder + name
                        print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Trying List {}\n".format(Colors.Color.GREEN + name))
                        sleep(5)
                        num_words = len(list(open(completefile, 'rb')))
                        f = open(completefile, "r", newline=None)
                        for password in tqdm(f, total=num_words,desc= "Cracking Password"):
                            attempt = attempt + 1
                            sleep(0.3)
                            origpassword = password.replace("\n","")
                            pwd = Hashing.Get.Decrypt(type,origpassword)
                            if pwd[0] == string or pwd[1] == string:
                                found = True
                                foundpass = origpassword
                                break
                            else:
                                found = False
                        if found == True:
                            break
                    if foundpass != "":
                        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Attempt n°{} Trying password {}: {}".format(Colors.Color.GREEN + str(attempt) + Colors.Color.WHITE,Colors.Color.GREEN + origpassword + Colors.Color.WHITE,Colors.Color.YELLOW2 + "Match"))
                        print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "The Password is: {}".format(Colors.Color.GREEN + foundpass))
                    else:
                        print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Password not found")
                        foundpass = "Not Found"
                    print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Result saved in: {}".format(Colors.Color.GREEN + report))
                    f = open(report,"a")
                    f.write("Decrypted Password: {}".format(foundpass))
                    f.close()
        inp = input(Colors.Color.WHITE + "\nPress enter to continue")
    
    @staticmethod
    def File():
        filesfolder = "Passwords/Default/"
        filesfolder2 = "Files"
        Controller.Size.Folder(filesfolder2,"Files","")
        found = False
        attempt = 0
        file_names = []
        Controller.Size.Folder(filesfolder,"Pwd",file_names)
        string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the file to open" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        foundpass = "" 
        while string == "":
            string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the filename" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Input archive/file: {}".format(Colors.Color.GREEN + string))
        if string == "Common" or string == "Unknown":
            pass
        else:
            report = "output/Archives/{}.txt".format(string)
            f = open(report,"w")
            f.write("Filename: {}\n\n".format(string))
            f.close()
            if found == False:
                    for name in file_names:
                        completefile = filesfolder + name
                        sleep(5)
                        path = "Files/" + string
                        if os.path.exists(path):
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Trying List {}\n".format(Colors.Color.GREEN + name))
                            if path.endswith(".pdf"):
                                newfile = "Extracted/Pdf/{}_extracted.pdf".format(string.replace(".pdf",""))
                                if os.path.isfile(newfile):
                                    os.remove(newfile)
                            num_words = len(list(open(completefile, 'rb')))
                            f = open(completefile, "r", newline=None)
                            for password in tqdm(f, total=num_words, desc= "Cracking Password"):
                                origpassword = password.replace("\n","")
                                if path.endswith(".zip") or path.endswith(".7z"):
                                    if found == False:
                                        attempt = attempt + 1 
                                        sleep(0.3)
                                        process = os.popen("7z x -y {} -p{} -oExtracted/Archives 2>&1|grep 'Everything is Ok'".format(path,origpassword))
                                        for message in process.readlines():
                                            if message == "\n":
                                                found = False
                                            elif message == "Everything is Ok\n":
                                                found = True
                                                foundpass = origpassword
                                                break 
                                    elif found == True:
                                        break
                                elif path.endswith(".rar"):
                                    if found == False:
                                        attempt = attempt + 1 
                                        sleep(0.3)
                                        process = os.popen("unrar -y x {} -p{} Extracted/Archives 2>&1|grep 'All OK'".format(path,origpassword))
                                        for message in process.readlines():
                                            if message == "\n":
                                                found = False
                                            elif message == "All OK\n":
                                                found = True
                                                foundpass = origpassword
                                                break
                                    elif found == True:
                                        break
                                elif path.endswith(".pdf"):
                                    if found == False:
                                        attempt = attempt + 1 
                                        sleep(0.3)
                                        process = os.popen("qpdf --password={} --decrypt {} {} 2>&1|grep ''".format(origpassword,path,newfile))
                                        status = process.close()
                                        if os.waitstatus_to_exitcode(status) != 1:
                                            found = False
                                        else:
                                            found = True
                                            foundpass = origpassword
                                            break
                                    elif found == True:
                                        break
                            if found == True:
                                if foundpass != "":
                                    print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Attempt n°{} Trying password {}: {}".format(Colors.Color.GREEN + str(attempt) + Colors.Color.WHITE,Colors.Color.GREEN + foundpass + Colors.Color.WHITE,Colors.Color.YELLOW2 + "Match"))
                                    print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "The Password is: {}".format(Colors.Color.GREEN + foundpass))
                                else:
                                    print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Password not found")
                                    foundpass = "Not Found"
                                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Result saved in: {}".format(Colors.Color.GREEN + report))
                                f = open(report,"a")
                                f.write("Password: {}".format(foundpass))
                                f.close()
                                break
                        else:
                            print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Archive {} doesn't exist on Folder: Files".format(Colors.Color.GREEN + string))
                            break
            inp = input(Colors.Color.WHITE + "\nPress enter to continue") 
                                
class Online:
    
    @staticmethod
    def Password():
        filesfolder = "Passwords/Default/"
        found = False
        attempt = 1
        file_names = []
        Controller.Size.Folder(filesfolder,"Pwd",file_names)
        reportname = substring = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert filename for the output ex 'Example.txt'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        while reportname == "" or reportname.endswith("/") or ".txt" not in reportname:
            reportname = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert filename for the output ex 'Example.txt'" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        auto = int(input(Colors.Color.BLUE + "\n[?]" + Colors.Color.WHITE + "Do you want to automatize the form recognizion process 'Works better on login pages'?(1)Yes(2)No" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
        foundpass = "" 
        agent = Useragent.Select.Useragent()
        proxy = Proxy.Select.Proxy()
        headers = Headers.Get.Agent(1,agent)
        report = "output/Web/Passwords/{}".format(reportname)
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Initial Useragent: {}".format(Colors.Color.GREEN + agent))
        print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Tor Proxy Ip: {}".format(Colors.Color.GREEN + proxy[0]))
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
                    string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                num = 0
                parms = "Undefined"
            elif parms == []:
                num = 0
                parms = "Undefined"
            elif string == "Not-Located":
                print(Colors.Color.RED + "\n[!]" + Colors.Color.WHITE + "Cannot retrieve request url")
                string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string == "":
                    string = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the url ex 'http://example.com' without the '/' at the end" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
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
                    for i in range(num):
                        string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the paramter name and value ex 'Username = test' Insert '<parameter> = password' to assign the password field" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        while string10 == "":
                            string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the paramter name and value ex 'Username = test' Insert '<parameter> = password' to assign the password field" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                        parameter = string10.split("=",1)[0].replace(" ","")
                        values2 = string10.rsplit("=",1)[1].replace(" ","")
                        if values2 == "password":
                            values3 = parameter
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "{}: {}".format(parameter,Colors.Color.GREEN + values2))
                            values2 = ""
                        else:
                            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "{}: {}".format(parameter,Colors.Color.GREEN + values2))
                        data.update({parameter:values2})
            elif reqt == "GET" or reqt == "Get" or reqt == "get":
                string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the complete query ex 'username=test name=name' Insert '<parameter>=password' to assign the password field " + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                while string10 == "":
                    string10 = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert the complete query ex 'username=test name=name' Insert '<parameter>=password' to assign the password field " + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                string = string + "?" + string10.replace(" ","&")
                typologi = "GET"
                data = {}
            if found == False:
                for name in file_names:
                    completefile = filesfolder + name
                    print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Trying List {}\n".format(Colors.Color.GREEN + name))
                    sleep(5)
                    num_words = len(list(open(completefile, 'rb')))
                    f = open(completefile, "r", newline=None)
                    await_t = 0
                    for password in tqdm(f, total=num_words, desc= "Cracking Password"):
                        password = password.replace("\n","").replace(" ","")
                        if reqt == "POST":
                            data[values3]= password
                            typologi = "POST"
                            req = Request.Create.Send(string,typologi,data,"status-code",headers,"",await_t,agent)
                        else:
                            string2 = string.replace("=password","={}".format(password))
                            req = Request.Create.Send(string2,typologi,data,"status-code",headers,"",await_t,agent)
                        if req[0] == "OK":
                            found = True
                            foundpass = password
                            f = open(report,"a")
                            f.write("Password: {}".format(foundpass))
                            f.close()
                            break
                        else:
                            found = False
                        sleep(0.3)
                        attempt = attempt + 1
                        await_t = await_t + 1
                        if await_t == 6:
                            await_t = 0
                    if found == True:
                        break
            if foundpass != "":
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Attempt n°{} Trying password {}: {}".format(Colors.Color.GREEN + str(attempt) + Colors.Color.WHITE,Colors.Color.GREEN + password + Colors.Color.WHITE,Colors.Color.YELLOW2 + "Match"))
                print(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "The Password is: {}".format(Colors.Color.GREEN + foundpass))
            else:
                print(Colors.Color.RED + "\n[-]" + Colors.Color.WHITE + "Password not found")
            print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Result saved in: {}".format(Colors.Color.GREEN + report))
        inp = input(Colors.Color.WHITE + "\nPress enter to continue")
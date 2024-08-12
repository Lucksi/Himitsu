# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core import Colors
from bs4 import BeautifulSoup as soup

class Get:

    @staticmethod
    def Http_form(content,url):
        try: 
            form_list = []
            parameters = []
            n = 0
            parser = soup(content, "html.parser")
            list1 = parser.find_all("form")
            for form in list1:
                n = n+1
                print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Form n° {}: {}".format(Colors.Color.GREEN + str(n) + Colors.Color.WHITE,form))
                form_list.append(form)
            if len(form_list):
                choice = int(input(Colors.Color.YELLOW + "\n[v]" + Colors.Color.WHITE + "Total Form found: {}\n".format(Colors.Color.GREEN + str(n) + Colors.Color.WHITE) + Colors.Color.BLUE + "\n[?]" + Colors.Color.WHITE + "Insert the form number" + Colors.Color.BLUE + "\n\n[Himitsu]" + Colors.Color.WHITE + "-->"))
                if choice != 0:
                    print(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE +"Getting form {} info\n".format(Colors.Color.GREEN + str(choice) + Colors.Color.WHITE))
                    form = list1[choice-1]
                    input_type = form.find_all("input")
                    if form.has_attr("method"):
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE +"Form Method: {}".format(Colors.Color.GREEN + form["method"]))
                        method = form["method"]
                    else:
                       method = "GET"
                       print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE +"Form Method: {}".format(Colors.Color.GREEN + method))
                    parameters.append(method)
                    if form.has_attr("action"):
                        print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE +"Form action: {}".format(Colors.Color.GREEN + form["action"]))
                        action = form["action"]
                        if "http://" in action or "https://" in action:
                            parameters.append(form["action"])
                        elif "/" in action or "//" in action:
                            parameters.append(url + "{}".format(form["action"]))
                        else:
                            parameters.append(url + "/{}".format(form["action"]))
                    else:
                        parameters.append("Not-Located")
                    for par in input_type:
                        if par["type"] == "hidden":
                            pass
                        else:
                            if par.has_attr("name"):
                                if par.has_attr("placeholder"):
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Parameter-name: " + Colors.Color.GREEN +  par["name"]+ Colors.Color.WHITE + " Parameter-description: " + Colors.Color.GREEN + par["placeholder"])#["name"].text
                                else:
                                    print(Colors.Color.YELLOW + "[v]" + Colors.Color.WHITE + "Parameter-name: " + Colors.Color.GREEN + par["name"])
                                parameters.append(par["name"])
                            else:
                                pass
            else:
                parameters = []
        except Exception as e:
            print(str(e))
        return parameters
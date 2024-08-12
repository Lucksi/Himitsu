# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from configparser import ConfigParser

class Get:
        
    @staticmethod
    def Value(parameter):
        configfile = "Configuration/Configuration.ini"
        parser = ConfigParser()
        parser.read(configfile)
        value = parser["Settings"][parameter]
        return value
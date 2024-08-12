# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2024 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import re as Regex
import hashlib

class Get:

    @staticmethod
    def Type(string):
        md5regex = r"\b(?!^[\d]*$)(?!^[a-fA-F]*$)([a-f\d]{32}|[A-F\d]{32})\b"
        base64regex = r"(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)"
        base32regex = r"/^([A-Z2-7=]{8})+$/"#r"^(?:[A-Z2-7]{8})*(?:[A-Z2-7]{2}={6}|[A-Z2-7]{4}={4}|[A-Z2-7]{5}={3}|[A-Z2-7]{7}=)?$"
        sha1regex = r"^[a-fA-F0-9]{40}$"
        sha224regex = r"^[a-fA-F0-9]{56}$"
        sha256regex = r"^[a-fA-F0-9]{64}$"
        sha384regex = r"^[a-fA-F0-9]{96}$"
        sha512regex = r"^[a-fA-F0-9]{128}$"
        if Regex.fullmatch(md5regex,string):
            type = "md5"
        elif Regex.fullmatch(sha1regex,string):
            type = "sha1"
        elif Regex.fullmatch(sha224regex,string):
            type = "sha224/sha3-224"
        elif Regex.fullmatch(sha256regex,string):
            type = "sha256/sha3-256"
        elif Regex.fullmatch(sha384regex,string):
            type = "sha384/sha3-384"
        elif Regex.fullmatch(sha512regex,string):
            type = "sha512/sha3-512"
        elif Regex.fullmatch(base64regex,string):
            type = "base64"
        elif Regex.fullmatch(base32regex,string):
            type = "base32"
        else:
            type = "Unknown"
        return type
    
    @staticmethod
    def Decrypt(type,origpassword):
        if type == "md5":
            password = hashlib.md5(origpassword.encode('utf-8')).hexdigest()
            password2 = ""
        elif type == "sha1":
            password = hashlib.sha1(origpassword.encode("utf-8")).hexdigest()
            password2 = ""
        elif type == "sha224/sha3-224":
            password = hashlib.sha224(origpassword.encode("utf-8")).hexdigest()
            password2 = hashlib.sha3_224(origpassword.encode("utf-8")).hexdigest()
        elif type == "sha256/sha3-256":
            password = hashlib.sha256(origpassword.encode("utf-8")).hexdigest()
            password2 = hashlib.sha3_256(origpassword.encode("utf-8")).hexdigest()
        elif type == "sha384/sha3-384":
            password = hashlib.sha384(origpassword.encode("utf-8")).hexdigest()
            password2 = hashlib.sha3_384(origpassword.encode("utf-8")).hexdigest()
        elif type == "sha512/sha3-512":
            password = hashlib.sha512(origpassword.encode("utf-8")).hexdigest()
            password2 = hashlib.sha3_512(origpassword.encode("utf-8")).hexdigest()
        return password,password2                           
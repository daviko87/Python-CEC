# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:05:20 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Ambato"
key = "LOxDnBrGPTyKcCQdMFL8oeeg9tmV0UZo"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
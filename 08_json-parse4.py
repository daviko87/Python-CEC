# -*- coding: utf-8 -*-
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "LOxDnBrGPTyKcCQdMFL8oeeg9tmV0UZo"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    jsonstatus = json_data["info"]["statuscode"]

    if jsonstatus == 0:
        print("API Status: " + str(jsonstatus) + " = A successful route call.\n")
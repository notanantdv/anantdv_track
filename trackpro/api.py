from __future__ import unicode_literals
import frappe
import requests
import json
from requests.structures import CaseInsensitiveDict

@frappe.whitelist()
def add_source_lead():
    vid = "25594130"
    # vid = vehid
    # vid = "25594130"
    vdn = "BDP-400"
    vdt = "Vehicle"
    
    url = "https://hst-api.wialon.com/wialon/ajax.html?svc=token%2Flogin&params={%22token%22%3A%222ea23c1f67c30ec4dbb8260c52d950b218EE1D8B77283AE5B8FD11186E19A715EF945CF1%22}"
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)


    
    sessiondata = json.loads(response.text)
    # print(sessiondata["eid"])
    # print(sessiondata.get("eid"))
    sid = sessiondata["eid"]
    
    url = f"https://hst-api.wialon.com/wialon/ajax.html?svc=core/search_item&sid={sid}&params=%7B%22id%22:{vid},%22flags%22:1025%7D"
    
    
    payload = {}
    headers = {
      'Authorization': 'Bearer 2ea23c1f67c30ec4dbb8260c52d950b218EE1D8B77283AE5B8FD11186E19A715EF945CF1'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    odo = data["item"]["lmsg"]["p"]["odometer"]
    long = data["item"]["lmsg"]["pos"]["x"]
    lat = data["item"]["lmsg"]["pos"]["y"]
    url = f"https://api.geoapify.com/v1/geocode/reverse?lat={lat}&lon={long}&format=json&apiKey=f7a05776fa714b52a1ebff90a3bf5076"
    payload = {}
    headers = {}
    resp = requests.request("GET", url, headers=headers, data=payload)
    resl = json.loads(resp.text)
    # print(data.text)
    loc = resl["results"][0]["formatted"]
    return odo,lat,long,loc
    # # return(data)
    # # print(response.text)
    # # print(str(data["item"]["lmsg"]["p"]["odometer"]))
    # url = f"https://api.geoapify.com/v1/geocode/reverse?lat={lat}&lon={long}&apiKey=349cb481664841199c928367b9ef88b9"
    # # payload = {}
    # # headers = {}

    # # response = requests.request("GET", url, headers=headers, data=payload)
    # # print(response.text)
    # headers = CaseInsensitiveDict()
    # headers["Accept"] = "application/json"
    # resp = requests.get(url, headers=headers)
    # print(resp.text)
    # return(odo,lat,long)
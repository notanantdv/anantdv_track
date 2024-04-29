from __future__ import unicode_literals
import frappe
import requests
import json

@frappe.whitelist()
def add_source_lead():
    vid = "25594130"
    vdn = "BDP-400"
    vdt = "Vehicle"
    
    url = "https://hst-api.wialon.com/wialon/ajax.html?svc=token%2Flogin&params={%22token%22%3A%222ea23c1f67c30ec4dbb8260c52d950b218EE1D8B77283AE5B8FD11186E19A715EF945CF1%22}"
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    # print(response.text)
    
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
    
    print(response.text)
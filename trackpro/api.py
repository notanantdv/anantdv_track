from __future__ import unicode_literals
import frappe
import requests
import json
from requests.structures import CaseInsensitiveDict

@frappe.whitelist()
def add_source_lead(vehid):
    # vid = "25594130"
    vid = vehid
    doc = frappe.db.get_list('Trackpro Settings',
    filters={
        'name': '0bc2652ae9'
    },
    fields=["trackpro_url","token"],
    
  )
    # vid = "25594130"
    vdn = "BDP-400"
    vdt = "Vehicle"
    token = doc[0].token
    urls = doc[0].trackpro_url

    url = urls+"?svc=token%2Flogin&params={%22token%22%3A%22"+token+"%22}"
    
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)


    
    sessiondata = json.loads(response.text)
    # print(sessiondata["eid"])
    # print(sessiondata.get("eid"))
    sid = sessiondata["eid"]
    
    url = urls+f"?svc=core/search_item&sid={sid}&params=%7B%22id%22:{vid},%22flags%22:1025%7D"
    
    
    payload = {}
    headers = {
      'Authorization': 'Bearer %{token}%'
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

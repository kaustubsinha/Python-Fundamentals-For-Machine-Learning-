# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 23:08:47 2018

@author: Kaustub Sinha
"""
import requests as rq
data = {
        "Phone_Number":"9983654545",
        "Name":"Kaustub Sinha",
        "College_Name":"Manipal University Jaipur",
        "Branch":"Jaipur"
        }

Req_send_url="http://13.127.155.43/api_v0.1/sending"
resp = rq.post(Req_send_url,json=data)
print(resp.text)

Req_Recv_url = "http://13.127.155.43/api_v0.1/receiving?Phone_Number=9983654545"
resp_Recv = rq.get(Req_Recv_url)
print(resp_Recv.text)

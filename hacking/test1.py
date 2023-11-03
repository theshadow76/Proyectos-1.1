from urllib import response
import requests
import json

while True:
    v1 = requests.get('https://lafase.cl/')
    v3 = requests.get('https://lafase.cl/wp-admin/admin-ajax.php')
    v2 = requests.post('https://lafase.cl/')
    print(v1, v2, v3)
    print(v3.request)
    print(requests.request)
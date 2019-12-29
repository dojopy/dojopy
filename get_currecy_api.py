import requests
import json

TOKEN = 'dfc4899fc100cb167072406ee001ac81'

def get_info_ip(ip):
    # uri = 'http://api.ipstack.com/{}?access_key={}&fields=country_code'.format(ip, TOKEN)
    uri = 'http://api.ipstack.com/{}?access_key={}'.format(ip, TOKEN)
    r = requests.get(uri, verify=False, timeout=5)
    if 200 <= r.status_code <= 300:
        print(r.json())
    else:
        print('error')
        return False


get_info_ip('200.106.89.5')

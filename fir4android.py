# -*- coding:utf-8 -*-
# Create by BoQin on 2018/12/06
import json
import os

import requests
import sys

PATH = ""

URL = "http://api.fir.im/apps"

TOKEN = "b3767abbc94ff93a935dec132fe93dd4"

BUNDLE_ID = "com.qts.customer"

HEADERS = {"Content-Type": "application/json"}

ICON = './timg.jpeg'

APK = './QtsCustomer-1.1.1-normal-release.apk'

post_data = {'type': 'android', 'bundle_id': '5aa5de3f548b7a283bd87939',
             'api_token': '3855da5aeac872749eba641d23c3f8c1'}

NIKE_NAME = 'TEST'

VERSION = '11'

BUILD = '11'

CHANGELOG = 'TEST'


# {"id":"5c246fe2959d6932bd0dc220","type":"android","short":"9auh","app_user_id":"5aa2206cca87a80c59135c72","storage":"qiniu","form_method":"POST","cert":{"icon":{"key":"7e9968c7e7a7475c40099133b13dc9d669c13550","token":"LOvmia8oXF4xnLh0IdH05XMYpH6ENHNpARlmPc-T:amzf-_XSYufJ0212aCy08lFxtf8=:eyJzY29wZSI6ImZpcmljb246N2U5OTY4YzdlN2E3NDc1YzQwMDk5MTMzYjEzZGM5ZDY2OWMxMzU1MCIsImNhbGxiYWNrVXJsIjoiaHR0cDovL2FwaS5maXIuaW0vYXV0aC9xaW5pdS9jYWxsYmFjaz9wYXJlbnRfaWQ9NWMyNDZmZTI5NTlkNjkzMmJkMGRjMjIwXHUwMDI2dGltZXN0YW1wPTE1NDU4OTE4MTBcdTAwMjZzaWduPTljNGM4XHUwMDI2b3JpZ2luYWxfa2V5PSIsImNhbGxiYWNrQm9keSI6ImtleT0kKGtleSlcdTAwMjZldGFnPSQoZXRhZylcdTAwMjZmc2l6ZT0kKGZzaXplKVx1MDAyNmZuYW1lPSQoZm5hbWUpXHUwMDI2b3JpZ2luPSQoeDpvcmlnaW4pXHUwMDI2aXNfY29udmVydGVkPSQoeDppc19jb252ZXJ0ZWQpIiwiZGVhZGxpbmUiOjE1NDU4OTI0MTAsInVwaG9zdHMiOlsiaHR0cDovL3VwLnFpbml1LmNvbSIsImh0dHA6Ly91cGxvYWQucWluaXUuY29tIiwiLUggdXAucWluaXUuY29tIGh0dHA6Ly8xODMuMTMxLjcuMyJdLCJnbG9iYWwiOmZhbHNlfQ==","upload_url":"https://upload.qbox.me","custom_headers":{}},"binary":{"key":"bbe28f36984afe2cc3b8cefa89d3f782f707fa29.apk","token":"LOvmia8oXF4xnLh0IdH05XMYpH6ENHNpARlmPc-T:gzC7dz-VLZxKUh81NMi_0yR-r98=:eyJzY29wZSI6InByby1hcHA6YmJlMjhmMzY5ODRhZmUyY2MzYjhjZWZhODlkM2Y3ODJmNzA3ZmEyOS5hcGsiLCJjYWxsYmFja1VybCI6Imh0dHA6Ly9hcGkuZmlyLmltL2F1dGgvcWluaXUvY2FsbGJhY2s_cGFyZW50X2lkPTVjMjQ2ZmUyOTU5ZDY5MzJiZDBkYzIyMFx1MDAyNnRpbWVzdGFtcD0xNTQ1ODkxODEwXHUwMDI2c2lnbj05YzRjOFx1MDAyNnVzZXJfaWQ9NWFhMjIwNmNjYTg3YTgwYzU5MTM1YzcyIiwiY2FsbGJhY2tCb2R5Ijoia2V5PSQoa2V5KVx1MDAyNmV0YWc9JChldGFnKVx1MDAyNmZzaXplPSQoZnNpemUpXHUwMDI2Zm5hbWU9JChmbmFtZSlcdTAwMjZvcmlnaW49JCh4Om9yaWdpbilcdTAwMjZuYW1lPSQoeDpuYW1lKVx1MDAyNmJ1aWxkPSQoeDpidWlsZClcdTAwMjZ2ZXJzaW9uPSQoeDp2ZXJzaW9uKVx1MDAyNmlzX3VzZV9tcWM9JCh4OmlzX3VzZV9tcWMpXHUwMDI2Y2hhbmdlbG9nPSQoeDpjaGFuZ2Vsb2cpXHUwMDI2cmVsZWFzZV90eXBlPSQoeDpyZWxlYXNlX3R5cGUpXHUwMDI2ZGlzdHJpYnV0aW9uX25hbWU9JCh4OmRpc3RyaWJ1dGlvbl9uYW1lKVx1MDAyNnN1cHBvcnRlZF9wbGF0Zm9ybT0kKHg6c3VwcG9ydGVkX3BsYXRmb3JtKVx1MDAyNm1pbmltdW1fb3NfdmVyc2lvbj0kKHg6bWluaW11bV9vc192ZXJzaW9uKVx1MDAyNnVpX3JlcXVpcmVkX2RldmljZV9jYXBhYmlsaXRpZXM9JCh4OnVpX3JlcXVpcmVkX2RldmljZV9jYXBhYmlsaXRpZXMpXHUwMDI2dWlfZGV2aWNlX2ZhbWlseT0kKHg6dWlfZGV2aWNlX2ZhbWlseSkiLCJkZWFkbGluZSI6MTU0NTg5NTQxMCwidXBob3N0cyI6WyJodHRwOi8vdXAucWluaXUuY29tIiwiaHR0cDovL3VwbG9hZC5xaW5pdS5jb20iLCItSCB1cC5xaW5pdS5jb20gaHR0cDovLzE4My4xMzEuNy4zIl0sImdsb2JhbCI6ZmFsc2V9","upload_url":"https://upload.qbox.me","custom_headers":{}},"mqc":{"total":5,"used":0,"is_mqc_availabled":true},"support":"qiniu","prefix":"x:"}}

def get_apk(path):
    """
    获取路径名
    :param path:
    :return:
    """

    for parent, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] == '.apk':
                print(filename)
                return os.path.join(parent, filename)


def upload_fir(apk):
    r = requests.post(URL, data=json.dumps(post_data), headers=HEADERS)
    if r.status_code == 201:
        res = json.loads(r.text)
        print(json.loads(r.text)['cert']['icon'])
        upload_file(res['cert']['icon']['upload_url'], res['cert']['icon']['key'], res['cert']['icon']['token'], ICON)
        upload_file(res['cert']['binary']['upload_url'], res['cert']['binary']['key'], res['cert']['binary']['token'],
                    apk)


def upload_file(url, key, token, file):
    param_data = {'key': key, 'token': token, 'x:name': NIKE_NAME, 'x:version': VERSION, 'x:build': BUILD,
                  'x:changelog': CHANGELOG}
    print(param_data)
    files = {'file': open(file, 'rb')}
    r = requests.post(url, data=param_data, files=files)
    print(r.status_code)
    print(r.text)


if __name__ == '__main__':
    # NIKE_NAME = sys.argv[1]
    # VERSION = sys.argv[2]
    # BUILD = sys.argv[3]
    upload_fir(get_apk('./'))
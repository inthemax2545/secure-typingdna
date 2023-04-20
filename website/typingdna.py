# import urllib.request, base64
# import json

# def send_typing_data(user_id, pattern):
#     base_url = 'https://api.typingdna.com'
#     apiKey = 'a56f6d5f10ad2a2c0d25d459362c0aa6'
#     apiSecret = '6db25bac774c07d5e2a78546879193e7'
#     tp = pattern

#     authstring = '%s:%s' % (apiKey, apiSecret)
#     base64string = base64.encodebytes(authstring.encode()).decode().replace('\n', '')
#     data = urllib.parse.urlencode({'tp':tp})
#     url = '%s/auto/%s' % (base_url, user_id)

#     request = urllib.request.Request(url, data.encode('utf-8'), method='POST')
#     request.add_header("Authorization", "Basic %s" % base64string)
#     request.add_header("Content-type", "application/x-www-form-urlencoded")

#     res = urllib.request.urlopen(request)
#     res_body = res.read()
#     return json.loads(res_body.decode('utf-8'))

import urllib.request
import base64
import json
import urllib.parse

def send_typing_data(user_id, pattern):
    base_url = 'https://api.typingdna.com'
    apiKey = 'a56f6d5f10ad2a2c0d25d459362c0aa6'
    apiSecret = '6db25bac774c07d5e2a78546879193e7'
    tp = pattern

    authstring = '%s:%s' % (apiKey, apiSecret)
    base64string = base64.b64encode(authstring.encode()).decode('utf-8')
    data = urllib.parse.urlencode({'tp':tp}).encode('utf-8')
    url = '%s/auto/%s' % (base_url, user_id)

    request = urllib.request.Request(url, data=data, method='POST')
    request.add_header("Authorization", "Basic %s" % base64string)
    request.add_header("Content-type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(request) as res:
        res_body = res.read().decode('utf-8')
        return json.loads(res_body)

import json
import os

import requests
def get_user_token():
    url = "{}generate-api-token".format(API_URL)
    payload = {
        "username": CLAAS_NAMESPACE,
        "password": NS_PASSWORD
    }
    r = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'})
    print r.text
    if r.status_code != 200:
        return None
    if "token" in json.loads(r.text):
        print "token is {}".format(json.loads(r.text)['token'])
        return json.loads(r.text)['token']
    else:
        return None

API_URL = os.getenv('API_URL','https://api-staging.alauda.cn')
if not API_URL.startswith('http') :
    API_URL = 'http://' + API_URL

API_VERSION = os.getenv("API_VERSION", "v1")

API_URL = "{}/{}/".format(API_URL, API_VERSION)
NS_PASSWORD = os.getenv('PASSWORD', 'alauda_staging')
CLAAS_NAMESPACE = os.getenv('NAMESPACE','testorg001')

API_TOKEN = os.getenv('API_TOKEN', get_user_token())
REGION_NAME = os.getenv('REGION_NAME', 'new_k8s_staging')


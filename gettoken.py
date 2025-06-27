import json
import requests
import base64 

def get_access_token():
    url = "https://id.cisco.com/oauth2/default/v1/token"

    #ご自身のclient_idとclient_secretを記載↓
    client_id = "xxx"
    client_secret = "xxxxx"

    payload = "grant_type=client_credentials" 
    value = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8') 
    headers = { 
        "Accept": "*/*", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Authorization": f"Basic {value}"
        } 
    token_response = requests.request("POST", url, headers=headers, data=payload) 
    token_data = token_response.json() 
    api_key = token_data.get('access_token')
    return api_key
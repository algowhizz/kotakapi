import json
import requests

kotak_ip = 'Your IP'
kotak_appId = 'Your app name'
user_id = 'Your user Id'
user_pwd = 'Your password'
consumer_key = 'Your consumer key'
access_token = 'Your app access token'



print('Generating session tokens')
headers = {
    'accept' : 'application/json',
    'consumerKey': consumer_key,
    'ip' : kotak_ip,
    'appId': kotak_appId,
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token,
    }
data = {"userid":user_id,"password":user_pwd}
response = requests.post('https://tradeapi.kotaksecurities.com/apim/session/1.0/session/login/userid', headers=headers, json=data)
user_ott = response.json()['Success']['oneTimeToken']
headers = {
    'accept' : 'application/json',
    'consumerKey': consumer_key,
    'ip' : kotak_ip,
    'appId': kotak_appId,
    'oneTimeToken':user_ott,
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + access_token,
    }
data = {"userid":user_id}
response = requests.post('https://tradeapi.kotaksecurities.com/apim/session/1.0/session/2FA/oneTimeToken',headers = headers,json = data)
user_session_token = response.json()['success']['sessionToken']


print('Sessions token generated:',user_session_token)


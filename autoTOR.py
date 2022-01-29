#from PIL import Image
from base64 import b64decode
#from hashlib import sha1
from io import BytesIO
import names
from hashlib import sha1
import names
import random
import hmac
import platform,socket,re,uuid 
import base64
import hmac
import time
import json
from hashlib import sha1
import secmail
import requests_random_user_agent
import random
import platform,socket,re,uuid
import json
import time
import os
import subprocess
import requests
from time import sleep
from bs4 import BeautifulSoup
from time import time as timestamp
import json
from os import path
#import amino
#from colored import fg, bg, attr

#from torpy.http.requests import TorRequests
from hashlib import sha1
import names
import random
import hmac
import platform,socket,re,uuid 
# -*- coding: utf-8 -*-

import time
import os
import subprocess




try:
    check_pip3 = subprocess.check_output('dpkg -s python3-pip', shell=True)
    if str('install ok installed') in str(check_pip3):
        pass
except subprocess.CalledProcessError:
    print('[+] pip3 not installed')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install python3-pip -y', shell=True)
    print('[!] pip3 installed succesfully')



try:

    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')
try:

    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:

    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")
def ma_ip():
    url='https://www.myexternalip.com/raw'
    get_ip= requests.get(url,proxies=dict(http='socks5://127.0.0.1:9050',https='socks5://127.0.0.1:9050'))
    return get_ip.text

def change():
    os.system("service tor reload")
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))


os.system("service tor start")




time.sleep(3)
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")
os.system("service tor start")
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    mac = hmac.new(bytes.fromhex('76b4a156aaccade137b8b1e77b435a81971fbd3e'), b"\x32" + identifier, sha1)
    return (f"32{identifier.hex()}{mac.hexdigest()}").upper()
 
def sig(data):
        #at=json.dumps(data)
        key='fbf98eb3a07a9042ee5593b10ce9f3286a69d4e2'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("32") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
 
 
 
 
 
 
def gen_email():
    mail = secmail.SecMail()
    email = mail.generate_email()
    return email
    
def upload(url):
    link = requests.get(url)
    result = BytesIO(link.content)
    return result
 
def get_message(email):
                try:
                    sleep(4)
                    f=email
                    mail = secmail.SecMail()
                    inbox = mail.get_messages(f)
                    for Id in inbox.id:
                        msg = mail.read_message(email=f, id=Id).htmlBody
                        bs = BeautifulSoup(msg, 'html.parser')
                        images = bs.find_all('a')[0]
                        url = (images['href']+'\n')
                        if url is not None:
                         print(url)
                         return url
                         #wget.download(url=url,out="code.png")
                except:
                    pass
            
def get_proxy_session():
    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050','https': 'socks5://127.0.0.1:9050'}
    return session

         
def register(session,user,nickname: str, email: str, password: str,deviceId: str):
        data = {
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent':user, 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
    }
        data=json.dumps(data)
        heads["NDC-MSG-SIG"]=sig(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        response = session.post(f"https://service.narvii.com/api/v1/g/s/auth/register", data=data, headers=heads)
        print(response.text)   
        
def request_verify_code(session,user,email: str,deviceId: str):
        data = {
            "identity": email,
            "type": 1,
            "deviceID": deviceId
        }
        heads={
    'Accept-Language': 'en-US', 
    'Content-Type': 'application/json; charset=utf-8', 
    'User-Agent': user, 
    'Host': 'service.narvii.com', 
    'Accept-Encoding': 'gzip',
    'Connection': 'Keep-Alive',
        }
        data = json.dumps(data)
        heads["Content-Length"] = str(len(data))
        heads["NDCDEVICEID"]=deviceId
        heads["NDC-MSG-SIG"]=sig(data)
        response = session.post(f"https://service.narvii.com/api/v1/g/s/auth/request-security-validation", data=data, headers=heads)
        print(response.text)
 
 

 
 
def threadit(session,user):
    deviceid=dev()
    values=gen_email()
    email=values
    nick=names.get_first_name()
    nick = "t.me/piececoin"
    req=request_verify_code(session,user,email=email, deviceId=deviceid)
    print(session.get(url="https://ifconfig.me/ip").text)
    #vcode=verify(values)
    register(session=session,user=user,nickname=nick, email=email, password="dfghjhdfg",deviceId=deviceid)
    p=input("hello:")
    register(session=session,nickname=nick, email=email, password="dfghjhdfg",deviceId=deviceid)
 

while True:
    change()
    session = get_proxy_session()
    
    for _ in range (3):
        s=requests.Session()
        user=s.headers["User-Agent"]
        threadit(session,user)
        

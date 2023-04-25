import requests
from lxml import html
from bs4 import BeautifulSoup
import json

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'cache-control': 'max-age=0',
    # 'cookie': 'SEARCH_SAMESITE=CgQI9JYB; AEC=AUEFqZfnTyBehR4dpB_1M5FzciFW38HDYu0W75nAPeXa4pN9VCNsam1BSw; 1P_JAR=2023-04-25-04; OGPC=19027681-1:; NID=511=CcS7okx5fKkU78VNO76BRj4kUzM9hRWRP8TnVyE50JDfuZZyc16UR71kHctf9r0HEe2ao6y3MCJkSaqwWfpLn2bsGwlILSTg3842TooREQkbHdmYAy1U1p4jDvT_mc6kkJC4niHHbY3MyDqyv7OWz7lE3r0iq7Zvo5mP_-w8HvMhk_mE_xKb-x6St8EaavIipxzrOTWzMsxSTV7JbaD5d5B_7tTYp_Aq1QETIZaY4VIrQNOaott81WWvOzTYMlqdrL9mInHJ24laB-ow_fwboiCShXrDg3C675ADmOE',
    'referer': 'https://duckduckgo.com/',
    'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

proxy_list=[]


#Collecting proxies from proxy-list.download
params = {
    'l': 'en',
    't': 'http',
}

response = requests.get('https://www.proxy-list.download/api/v2/get', params=params)
for i in (response.json().get('LISTA')):
    ip=i.get('IP')
    port=i.get('PORT')
    ipnport=ip+":"+port
    if ipnport not in proxy_list:
        proxy_list.append(ipnport)

#Collecting proxies from free.proxy.list.net
response=requests.get('https://free-proxy-list.net/',headers=headers)
soup=BeautifulSoup(response.text,'html.parser')
tr=soup.find_all('tbody')[0].find_all('tr')
for i in range(len(tr)):
    ip=(tr[i].find_all('td')[0].text)
    port=(tr[i].find_all('td')[1].text)
    if ip+':'+port not in proxy_list:
        proxy_list.append(ip+':'+port)
print("Total no. of Proxies="+str(len(proxy_list)))
print('\n')


# **********************(INPUT)************************
NUM_TRIALS=10
TARGET_URL='https://www.google.com'
OUTPUT_FILENAME='Working_proxy.json'


#Checking proxy
usable=[]   
usable_100=[]   
for i in range(len(proxy_list)):
    print("Trying proxy no."+str(i+1)+"..")
    print(proxy_list[i])
    print('\n')
    proxy=proxy_list[i]
    for j in range(NUM_TRIALS):
        try:
            response_1 = requests.get(TARGET_URL, proxies={"http":proxy, "https":proxy}, headers=headers,timeout=15)
            print("Proxy no."+str(i)+", Test-"+str(j+1))
            if j==NUM_TRIALS-1:
                print(NUM_TRIALS,"Test passed")
                usable.append(proxy_list[i])
                print('\n')
                with open(OUTPUT_FILENAME,'w',encoding='utf-8') as f:
                        json.dump(usable,f,indent=2,ensure_ascii=False)
        except:
            print("Proxy no."+str(i+1)+" failed")
            print('\n')
            break


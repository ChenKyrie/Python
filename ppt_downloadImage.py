# 导入 requests 包
import requests
import re
import os
import urllib.request
from bs4 import BeautifulSoup


cookies = {'over18':'1'}
r=requests.get('https://www.ptt.cc/bbs/Beauty/search?q=recommend%3A10',cookies=cookies)

soup=BeautifulSoup(r.text, 'html.parser')

def filterItemHtml(soup):
        data = []
        results = soup.find_all('div', {'class' : 'r-ent'})
        for item in results:
            try:
                title = item.find('a').contents[0]
                if re.search('.+帥哥.+', title):
                    continue
                link = 'https://www.ptt.cc'+str(item.find('a')['href'])
                date = item.find('div',{'class':'date'}).contents[0].replace(' ','')
                itemId = str(item.find('a')['href']).split('/')[-1]
                data.append({'title':title,'link':link,'date':date,'linkId':itemId})
            except:
                continue
        #print(data)
        #print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))
        return data
# 发送请求
#x = requests.get('https://www.ptt.cc/bbs/Beauty/index.html')
def getImageLink(soup):
    data = []
    #移除推文
    for div in soup.find_all("div", {'class':'push'}):
        div.decompose()
    #找所有的a tag，比對是否為imgur.com
    results = soup.find_all('a')
    for item in results:
        try:
            if re.search('https://(i\.)?imgur.com/.+\.(jpg|jpeg|png)', item.get('href').lower()):
                data.append(item.get('href'))
        except:
            continue
    #print(data)
    #print(json.dumps(data, indent=4, sort_keys=True,ensure_ascii=False))
    return data

def downloadImage(links,path):
    print('download start')
    print('download image...(0/{links})'.format(links=len(links)),end='\r')
    if not os.path.exists(path):
        os.makedirs(path)
    path
    files={
        'path':path,
        'fileList':[]
    }
    count = 0
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    for link in links:
        count+=1
        urllib.request.urlretrieve(link, os.path.join(path,link.split('/')[-1]))
        print('download image...({count}/{links})'.format(count=count,links=len(links)),end='\r')
        files['fileList'].append(link.split('/')[-1])
    print('download image...({count}/{links})...ok'.format(count=count,links=len(links)))
    return files
# 返回网页内容
#print(r.text)
#print(soup.prettify())
a=filterItemHtml(soup)
#print(a)

r=requests.get(a[0]['link'],cookies=cookies)
soup=BeautifulSoup(r.text, 'html.parser')
b=getImageLink(soup)
#print(b)

path='downloads'
downloadImage(b,path)

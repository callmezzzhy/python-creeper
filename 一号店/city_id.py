from bs4 import BeautifulSoup
import requests
import os
import re
path=os.path.dirname(os.path.abspath(__file__))
with open(path +'/city.html',encoding='utf-8')as f:
    html=f.read()

def get_city_id():
    city_id={}
    soup=BeautifulSoup(html,'lxml')
    citys=soup.find_all('a')
    for city in citys:
        name=city.text.replace('市','')
        proid=city['data-provinceid']
        cityid=city['data-cityid']
        city_id[name]=cityid
    return city_id
def get_idinfo(ids):
    url='http://www.yhd.com/homepage/getCityById.do?callback=jsonp_getCityById9&cityId={}'.format(ids)
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')

    soups=re.sub(r'<html><body><p>|</p></body></html>', '', str(soup))

    l=soups[soups.find('"areaId"')+1:-2]
    infos=l.split(',')
    info_list={}
    for info in infos:

        info_list[info.split(':')[0].replace('"','')]=info.split(':')[1]

    return info_list

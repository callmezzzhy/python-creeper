import requests
import json
import re
from bs4 import BeautifulSoup
from city_id import get_city_id,get_idinfo
def get_html_text(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ValueError('errors')
def num_detial(ids,provinceID,cityID,areaID,townID):
    url='http://c0.3.cn/' \
        'stock?extraParam=%7B%22originid%22:%221%22%7D&ch=1&callback=jQuery111301418887452351818_1507952646611&skuId={}&' \
        'area={}_{}_{}_{}&cat=1316%2C1381%2C1389&buyNum=1&venderId=1000003747&fqsp=0&_=1507952646612'.format(ids,provinceID,cityID,areaID,townID)
    text=get_html_text(url)
    info=text[text.find('{')+1:-2]
    num_info={}
    l=info.split(',')
    for i in l:
        try:
            num_info[i.split(':')[0].replace('"','')]=i.split(':')[1]
        except:
            continue
    nums=num_info["stockDesc"]
    num=nums[nums.find('>')+1:nums.find('>')+3]
    return num
def parser_info(url,provinceID,cityID,areaID,townID):
    parser_infos=[]
    html=requests.get(url)
    soup=BeautifulSoup(html.text,'lxml')
    infos=soup.find_all('div',class_='mod_search_pro')
    for info in infos:
        name=info.find('p',class_='proName clearfix').a.text.strip()
        price=info.find('em',class_='num').text.strip()
        address='http'+ info.find('p',class_='proName clearfix').a['href']
        ids='http'+ info.find('p',class_='proName clearfix').a['id']
        iid=re.sub(r'httppdlink2_','',ids)
        num=num_detial(iid,provinceID,cityID,areaID,townID)
        parser_infos.append({'name':name,'price':price,'num':num,'address':address})
    return parser_infos
def save_info(infos):
    with open('info_list.txt','w+',encoding='utf-8')as f:
        for info in infos:
            f.write('名字：{}\t 价格：{}\t \n货品：{}\t地址：{}\t\n'.format(info['name'],info['price'],info['num'],info['address']))
def main():
    stock=input('请输入你要查找的商品名称:')
    prov=input('请输入你要查找的城市：')
    city=get_city_id()
    city_id=city[prov]
    id_info=get_idinfo(city_id)
    provinceID=id_info['provinceId']
    cityID=id_info['cityId']
    areaID=id_info['areaId']
    townID=id_info['townId']
    url='http://search.yhd.com/c0-0/k'+stock
    print('正在进入1号店，请稍等...')
    infos=parser_info(url,provinceID,cityID,areaID,townID)
    save_info(infos)
    print('已经保存')
if __name__=='__main__':
    main()
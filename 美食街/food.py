import requests
from bs4 import BeautifulSoup
# 地方小吃入口url
Top_food_url = 'http://www.meishij.net/china-food/xiaochi/'

# 家常菜谱入口url
Home_food_url = 'http://www.meishij.net/chufang/diy/'

# 中华菜系入口url
China_food_url = 'http://www.meishij.net/china-food/caixi/'

# 外国菜入口url
Foreign_food_url = 'http://www.meishij.net/chufang/diy/guowaicaipu1/'

def get_html(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'
def parse_city_id(url):
    top={}
    html=get_html(url)
    nams=[]
    if html!='error':
        soup=BeautifulSoup(html,'lxml')
        if soup.find('dl',class_='listnav_dl_style1 w990 bb1 clearfix'):
            cityids=soup.find('dl',class_='listnav_dl_style1 w990 bb1 clearfix')
        else:
            cityids=soup.find('dl',class_='listnav_dl_style1 w990 clearfix')
        areas=cityids.find_all('a')
        for area in areas:
            top[area.text.strip()]=area['href']
            nams.append(area.text.strip())
        return top,nams
    else:
        print('error')

def get_info(url,pages=1):
    urls=[]
    for page in range(int(pages)):
        urls.append('{}?&page={}'.format(url,page))
    for uurl in urls:
        html=get_html(uurl)
        soup=BeautifulSoup(html,'lxml')
        info_list=[]
        infos=soup.find_all('div', class_='listtyle1')
        for info in infos:
            name=info.find('div',class_='c1').strong.text
            alter=info.find('div',class_='c1').em.text
            ditail=info.find_all('li')[0].text+'\t'+info.find_all('li')[1].text
            setup=info.find('a',class_='big')['href']
            imag=info.find('img',class_='img')['src']
            info_list.append({'name':name,'alter':alter,'ditail':ditail,'setup':setup,'imag':imag})
            yield info_list

def save_info(infos):
    with open ('info_list.txt','w+',encoding='utf-8')as f:
        for info in infos:
            f.write('菜名:{}\t作者:{}\t\n详情:{}\n步骤:{}\n图片:{}\n'.format(info['name'],info['alter'],info['ditail'],info['setup'],info['imag']))

def main():
    urllist={'地方小吃': Top_food_url, '家常菜谱': Home_food_url, '中华菜系' : China_food_url, '外国菜': Foreign_food_url}
    sort=input('请输入你想知道的菜谱分别输入为：地方小吃、家常菜谱、中华菜系、外国菜：')
    url=urllist[sort]
    print(url)
    item,names=parse_city_id(url)
    print('该菜谱下有：{}'.format(names))
    name=input('请输入你想了解的其中一项：')
    page=input('输入吃货个数：')
    urls=item[name]
    info_list=get_info(urls,pages=page)
    print('正在收集')
    for info in info_list:
        save_info(info)
    print('保存成功')
if __name__=='__main__':
    main()






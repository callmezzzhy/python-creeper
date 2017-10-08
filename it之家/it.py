#coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
import re
import time
def parse_news_id(cate,page_start):
    '''
    找到当前分类下的首页文章id
    '''
    data={
        'categoryid': cate,
        'type': 'pccategorypage',
        'page': '1',
    }
    l=[]
    for page in range(page_start,page_start+11):
        data['page']=str(page)
        try:
            r=requests.post('http://iphone.ithome.com/ithome/getajaxdata.aspx',data=data)
            soup=BeautifulSoup(r.text,'lxml')
            list_1=soup.find_all('li')
            for l in list_1:
                name=l.find('div',class_='block').h2.text[0:-6]
                names=re.sub(r'今|日','',name)
                content=l.find('div',class_='memo').p.text.strip()
                new=l.find('a',class_='list_thumbnail')
                #l=new['href'].split('/')[-1].replace('.htm','')
                yield names,content,new['href'],new['href'].split('/')[-1].replace('.htm','')
        except:
            return  None


def get_hot_content(new_id,url):
    '''
    '''
    info_list=[]
    data={
     'newsID': new_id,
    'type': 'hotcomment'
    }

    data1={
    'newsID': new_id,
    'hash':'C86D050F0FF8E039',
    'type':'commentpage',
    'page':'1',
    'order':'false'
    }
    header={
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Connection':'keep-alive',
        'Host':'dyn.ithome.com',
        'Referer':url,
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
    }

    cookie={
        'ASP.NET_SessionId':'fqqlqo1lya4etxsva20dlnxg',
        'BEC':'40E667F5B72629C68E12808D6F92AE9A|WdhtV|Wdhp+',
        'Hm_lvt_f2d5cbe611513efcf95b7f62b934c619':'1507279520',
        'Hm_lpvt_f2d5cbe611513efcf95b7f62b934c619':'1507355907',
        'Hm_lvt_cfebe79b2c367c4b89b285f412bf9867':'1507279520',
        'Hm_lpvt_cfebe79b2c367c4b89b285f412bf9867':'1507355925'
    }
    try:
        r=requests.post('https://dyn.ithome.com/ithome/getajaxdata.aspx',data=data)
        r.encoding='utf-8'
        r.raise_for_status()
        soup=BeautifulSoup(r.text,'lxml')
        comment_list=soup.find_all('li',class_='entry')
        for comment in comment_list:
            content=comment.find('p').text.strip()
            name=comment.find('strong',class_='nick').a.text.strip()
            info=comment.find('div',class_='info rmp').find_all('span')
            if len(info)==2:
                phone_info=info[0].text
                local_info=info[1].text.split('\xa0')[0].replace('IT之家', '').replace('网友', ' ')
                time_info=info[1].text.split('\xa0')[1]
            elif len(info)==1:
                phone_info='暂无'
                local_info=info[0].text.split('\xa0')[1].replace('IT之家', '').replace('网友', ' ')
                time_info=info[0].text.split('\xa0')[1]
            else:
                phone_info='暂无'
                local_info='暂无'
                time_info='暂无'
            info_list.append({'name':name,'content':content,'phone_info':phone_info,'local_info':local_info,'time_info':time_info})
        return info_list
    except:
        return None
def clear_db():
        db=pymysql.connect('localhost','root','123456','ithome')
        cursor=db.cursor()
        sql1= "DELETE FROM itcontent"
        sql2="alter table itcontent auto_increment=1"
        cursor.execute(sql1)
        cursor.execute(sql2)
        db.commit()
        db.close()
def save_content(contents,names,cont):
        for content in contents:
            try:
                db=pymysql.connect('localhost','root','123456','ithome',use_unicode=True,charset="utf8mb4")
                cursor=db.cursor()
                sql5="ALTER TABLE itcontent CONVERT TO CHARACTER SET utf8mb4"
                sql3="""INSERT INTO itcontent(帖子,文本,名字,内容,手机信息,位置,时间)
                    VALUES(%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql5)
                cursor.execute(sql3,(names,cont,content['name'],content['content'],content['phone_info'],content['local_info'],content['time_info']))
                db.commit()
            finally:
                db.close()

        print('存储成功')
'''
def decorate(fun):
    def timecounter(*args):
        start=time.perf_counter()
        result=fun(*args)
        timess=time.perf_counter()
        times=timess-start
        name=fun.__name__
        number=','.join(repr(ar) for ar in args)
        print('[{:.8f}s] {}({})->{}'.format(times,name,number,result))
    return timecounter

@decorate
'''
def main(page_list):
    ID='56'
    new_id_list=parse_news_id(ID,page_list)
    clear_db()
    for a,b,c,d in new_id_list:
        contents=get_hot_content(d,c)
        if contents:
            save_content(contents,a,b)
        else:
            print('出错啦~')
if __name__=='__main__':
    from multiprocessing import Pool
    pool=Pool(processes=3)
    group=([x for x in range(0,10)])
    pool.map(main,group)
    time.process_time()
    pool.close()
    pool.join()


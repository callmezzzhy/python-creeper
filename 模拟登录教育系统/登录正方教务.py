import requests
import bs4
import os

from PIL import Image
def get_post_ddata(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/61.0.3163.79 Safari/537.36'}
    html=requests.get(url,headers=headers)
    soup=bs4.BeautifulSoup(html.text,'lxml')
    __VIEWSTATE=soup.find('input', attrs={'name': '__VIEWSTATE'})['value']
    print(__VIEWSTATE)
    pic=requests.get('http://jwgl.gdut.edu.cn/CheckCode.aspx').content
    with open('验证码.png','wb')as f:
        f.write(pic)
    imag=Image.open({}+'/'+'验证码.png'.format(os.getcwd()))
    imag.show()

    data={
            'txtUserName': '',
            'Textbox1': '',
            'TextBox2': '',
            'txtSecretCode': "",
            '__VIEWSTATE': '',
            # 这里我将radio栏--学生 encode成gbk编码，以符合数据的要求
            'RadioButtonList1': '\xd1\xa7\xc9\xfa',
            'Button1': '',
            'lbLanguage': '',
            'hidPdrs': '',
            'hidsc': '',
    }

    data['__VIEWSTATE']=__VIEWSTATE
    data['txtSecretCode']=input('请输入图片验证码')
    data['txtUserName']=input('请输入学号')
    data['TextBox2']=input('请输入密码')
    return data

def login(url,data):
    s=requests.session()
    s.post(url,data=data)
    return s
base_url='http://jwgl.gdut.edu.cn/default2.aspx'
data=get_post_ddata(base_url)
print(data)
log=login(base_url,data)


test=log.get('http://jwgl.gdut.edu.cn/xs_main.aspx?xh=14200406101')
soup = bs4.BeautifulSoup(test.text, 'lxml')
try:
    name = soup.find('span', attrs={'id': 'xhxm'}).text
except:
    name = '登录失败 '
print(name)
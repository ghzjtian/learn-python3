#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
#Linux中要把该文件的权限改为  chmod a+x  ,才能双击打开



__author__ = 'Wayne'
import urllib.request
import os
import re
import base64

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
    response = urllib.request.urlopen(req)
    return response.read()

def get_page(url):

    html = url_open(url).decode('utf-8')
    # html = '<a title="Older Comments" href="//jandan.net/ooxx/page-50689337#comments" class="previous-comment-page">'
    # html = '<span class="break">' \
    #        '</span>'\
    #         '<div class="cp-pagenavi">'\
    #         '<a title="Older Comments" href="//jandan.net/ooxx/page-50689337#comments" class="previous-comment-page">下一页</a>' \
    #         '<a title="Older Comments" href="//jandan.net/ooxx/page-506237#comments" class="previous-comment-page">下一页</a>' \
    #         '</div>'\
    #         '</div>'
    # print(html)
    pattern = r'[href="//jandan.net/ooxx/page-]{1}(\d{1,8})#comments' #正则表达式寻找页面地址
    # pattern = r'Older'
    m = re.findall(pattern, html)
    if(m):
        print(m)
        return int(m[1])
    else:
        return -1


def find_imgs(page_url):

    # pattern = r'<img src="(.*?\.jpg)"'
    # pattern = r'<span class="img-hash">(.*?)</span>"'
    pattern = r'\<span\sclass=\"img-hash\"\>'

    html = url_open(page_url).decode('utf-8')
    #图片的 url 经过了 base64 编码
    # html = '<span class="img-hash">Ly93eDEuc2luYWltZy5jbi9tdzYwMC8wMDc2QlNTNWx5MWZybWNuY3QwZGZqMzBlNjBrMDB0Zi5qcGc=</span>'

    img_addrs = re.findall(pattern,html)
    print("img_addrs:",img_addrs)
    return img_addrs


def save_imgs(img_addrs,page_num,folder):
    if not os.path.exists(str(page_num)):
        os.mkdir(str(page_num))
    os.chdir(str(page_num))
    for i in img_addrs:
        a = base64.b64decode(i)
        pattern = r'sinaimg.cn/mw600/(.*?).jpg'
        filename = a.split('/')[-1]
        image = url_open(i)
        with open(filename,'wb') as f:
            f.write(image)
            f.close()


def download_mm(folder='ooxx',pages=2):

    if not os.path.exists(folder):
        os.mkdir(folder) #新建文件夹

    os.chdir(folder) #跳转到文件夹
    folder_top = os.getcwd() #获取当前工作目录
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url) #获取网页最新的地址

    print("page_num", page_num)
    if(page_num < 0):
        return

    for i in range(pages):
        page_num -= i #递减下载几个网页
        page_url = url + 'page-' + str(page_num) + '#comments' #组合网页地址
        img_addrs = find_imgs(page_url) #获取图片地址
        save_imgs(img_addrs,page_num,folder) #保存图片
        os.chdir(folder_top)

if __name__ == '__main__':
    # folder = input("Please enter a folder(default is 'ooxx'): " )
    # pages = input("How many pages do you wan to download(default is 10): ")
    folder = 'test'
    pages = 1
    download_mm(str(folder),int(pages))


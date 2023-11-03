# 1.获取界面部分
import urllib

url = "https://www.baidu.com"
useragent = ""


def askURL(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        html = response.read()
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 2.解析页面
from bs4 import BeautifulSoup
import re


def getData(baseurl):
    # 构造正则表达式
    findLink = re.compile(r'< a href = "(.*?)">')
    findImgSrc = re.compile(r'< img. * src = "(.*?)"', re.S)
    findTitle = re.compile(r'< span class = "title">(.*)</span>')
    findRating = re.compile(r'< span class = "rating_num" property = "v:average">(.*)</span>')
    findJudge = re.compile(r'< span >(\d*)人评价</span>')
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    findBd = re.compile(r'<p class= "">(.*?)</p>', re.S)
    remove = re.compile(r'|\n|</br>|\.*')
    datalist = []
    for page in range(0, 10):
        url = baseurl + str(page * 25)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            ctitle = titles[0]
            data.append(ctitle)
            if (len(titles) == 2):
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append('')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace(".", "")
                data.append(inq)
            else:
                data.append('')
            bd = re.findall(findBd, item)[0]
            bd = re.sub(remove, "", bd)
            bd = re.sub('<br(\s+)?\/?>(\s+)?', "", bd)
            bd = re.sub('/', "", bd)
            data.append(bd.strip())
            datalist.append(data)
            return datalist


# 3.存储数据
import xlwt


def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣电影 Top250', cell_overwrite_ok=True)
    cols = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价数', '概况', '相关信息')
    for col in range(0, 8):
        sheet.write(0, col, cols[col])
    for row in range(0, 250):
        data = datalist[row]
        for col in range(0, 8):
            sheet.write(row + 1, col, data[col])
    book.save(savepath)


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# df = pd.read_excel("")
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.size'] = 20
# plt.figure(figsize=(20, 5))
# plt.subplot(1, 2, 1)
# plt.scatter(df['评分'], range(1, 251))
# plt.xlabel('评分')
# plt.ylabel('排名')
# plt.gca().invert_yaxis()
# plt.subplot(1, 2, 2)
# plt.hist(df['评分'], bins=15)

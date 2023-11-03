import requests
import re

url = 'http://www.jryj.org.cn/CN/volumn/volumn_101.shtml'
r = requests.get(url)
print(r.text)
text = r.text
re.findall("<a>")
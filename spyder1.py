import requests
import re
url = 'http://www.jryj.org.cn/CN/volumn/volumn_3.shtml'
r = requests.get(url)
text = r.text
div = re.findall(r'<div(.*?)</div>'.text)
ewords = re.findall(r'>(.*?)</a>', div)
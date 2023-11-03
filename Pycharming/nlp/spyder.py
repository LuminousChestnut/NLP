def spyder(url, useragent=""):
    import requests
    getter = requests.get(url, headers=useragent)
    rawtext = getter.text
    return rawtext


import replacer
replacer("asd", ['a'])

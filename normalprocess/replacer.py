# -*- coding: utf-8 -*-
def replacer(replaceString, replaceWordList, flagDisplay=0):
    """
    2023-10-27 v0.1
    replaceString(str) ：需要替换的字符串
    replaceWordList(list) : 替换的列表
    flagDisplay(int) ：是否显示旗帜（运行成功旗帜为0，运行失败旗帜为1）
    """

    try:
        for word in replaceWordList:
            replaceString = replaceString.replace(word, "")
        flag = 0
    except(ValueError, SyntaxError):
        flag = 1
    if flagDisplay == 0:
        replacer_x_flag = flag
        replacer_x_String = replaceString


print("我的撒大")

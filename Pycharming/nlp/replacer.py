def replacer(replaceString, replaceWordList):
    """
    2023-11-03 v0.2
    replaceString(str) ：需要替换的字符串
    replaceWordList(list) : 替换的列表
    flagDisplay(int) ：是否显示旗帜（运行成功旗帜为0，运行失败旗帜为1）
    """

    try:
        for word in replaceWordList:
            replaceString = replaceString.replace(word, "")
    except(ValueError, SyntaxError):
        print("replacer 发生错误")

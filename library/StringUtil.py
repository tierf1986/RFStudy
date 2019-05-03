# -*- coding: utf-8 -*-
import re
import datetime
import time


class StringUtil():
    def __init__(self):
        pass

    def getNumfromString(self, s):
        return re.findall(r"\d+[,\d{3}]+", s)


if __name__ == '__main__':
    s = '百度为您找到相关结果约1,580,000个'
    print(StringUtil().getNumfromString(s))

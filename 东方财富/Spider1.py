import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import random


class Spider:
    def __init__(self, url):
        proxy = ["112.115.57.20:3128"]
        self._url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.proxies = {"http": random.choice(proxy)}
    def get(self):
        # rq  = requests.session()
        get_content = requests.get(url=self._url, headers=self.headers)
        get_content.encoding = get_content.apparent_encoding
        if get_content.raise_for_status() == None:
            return get_content.text
        else:
            print(get_content.raise_for_status())
            return exit()

    def resolving(self):
        soup = BeautifulSoup(self.get(),'lxml')
        return soup
    def main(self):
        pass
s = Spider('http://shop.cmbc.com.cn/mall/')
print(s.resolving())

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt


class Spider:
    def __init__(self, url):
        proxy = ["112.115.57.20:3128"]
        self._url = url
        self.headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        self.proxies = {"http": random.choice(proxy)}

    def get(self):
        get_content = requests.get(url=self._url, headers=self.headers)
        get_content.encoding = get_content.apparent_encoding
        if get_content.raise_for_status() == None:
            return get_content.text
        else:
            print(get_content.raise_for_status())
            return exit()

    def resolving(self):
        soup = BeautifulSoup(self.get(), 'lxml')
        return soup

    def post(self, content):
        post_content = requests.session().post(content)


if __name__ == "__main__":
    # the url of the function
    code = []
    name = []
    net_value = []
    accumulated_net = []
    day_raise = []
    week_raise = []
    one_month_raise = []
    three_month_raise = []
    six_month_raise = []
    one_year_raise = []
    two_year_raise = []
    three_year_raise = []
    this_year_raise = []
    running_raise = []
    for page in range(111):
        url_function = 'http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=' \
                       '2018-12-29&ed=2019-12-29&qdii=&tabSubtype=,,,,,&pi={}&pn=50&dx=1&v=0.7186969673210204'.format(
            page)
        spider_function = Spider(url_function)
        soup_function = spider_function.resolving()
        content = re.findall(r'\[.*\]', str(soup_function))[0].split('"')[1:-1]
        for each in content:
            if each != ',':
                for ix, c in enumerate(each.split(',')):
                    if ix == 0:
                        code.append(c)
                    elif ix == 1:
                        name.append(c)
                    elif ix == 4:
                        net_value.append(c)
                    elif ix == 5:
                        accumulated_net.append(c)
                    elif ix == 6:
                        day_raise.append(c)
                    elif ix == 7:
                        week_raise.append(c)
                    elif ix == 8:
                        one_month_raise.append(c if c != '' else None)
                    elif ix == 9:
                        three_month_raise.append(c if c != '' else None)
                    elif ix == 10:
                        six_month_raise.append(c if c != '' else None)
                    elif ix == 11:
                        one_year_raise.append(c if c != '' else None)
                    elif ix == 12:
                        two_year_raise.append(c if c != '' else None)
                    elif ix == 13:
                        three_year_raise.append(c if c != '' else None)
                    elif ix == 14:
                        this_year_raise.append(c if c != '' else None)
                    elif ix == 15:
                        running_raise.append(c if c != '' else None)
        import time

        print('已经完成第{}页'.format(page + 1))
        time.sleep(1)
    Dataframe_func = pd.DataFrame(
        {'code': code, 'name': name, 'net_value': net_value, 'accumulate_net': accumulated_net, 'day_raise': day_raise, \
         'week_raise': week_raise, 'one_month_raise': one_month_raise, 'three_month_raise': three_year_raise,
         'six_month_raise': six_month_raise, 'one_year_raise': one_year_raise, 'two_year_raise': two_year_raise,
         'three_year_raise': three_year_raise, 'this_year_raise': this_year_raise, 'running_raise': running_raise, })

    print(Dataframe_func)

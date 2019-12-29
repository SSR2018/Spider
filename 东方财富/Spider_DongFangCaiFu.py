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
        #headers
        self.headers = {
            'Accept': '* / *',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Connection': 'keep - alive',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        #代理ip
        self.proxies = {"http": random.choice(proxy)}

    def get(self):
        get_content = requests.get(url=self._url, headers=self.headers)
        get_content.encoding = get_content.apparent_encoding
        if get_content.raise_for_status() == None:
            return get_content.text
        else:
            print(get_content.raise_for_status())
            return exit()
    #解析
    def resolving(self):
        soup = BeautifulSoup(self.get(), 'lxml')
        return soup
    #post
    def post(self, content):
        post_content = requests.session().post(content)

def func_spider(pages =112):
    # the url of the function
    code = []
    name = []
    net_value = []  # 净值
    accumulated_net = []  # 累计净值
    day_raise = []  # 日增长率
    week_raise = []  # 周
    one_month_raise = []  # 近1月
    three_month_raise = []  # 近3月
    six_month_raise = []  # 近6月
    one_year_raise = []  # 近1年
    two_year_raise = []  # 近2年
    three_year_raise = []  # 近3年
    this_year_raise = []  # 今年
    running_raise = []  # 成立来
    for page in range(pages):
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
                        net_value.append(eval(c))
                    elif ix == 5:
                        accumulated_net.append(eval(c))
                    elif ix == 6:
                        day_raise.append(eval(c))
                    elif ix == 7:
                        week_raise.append(eval(c))
                    elif ix == 8:
                        one_month_raise.append(eval(c) if c != '' else 0)
                    elif ix == 9:
                        three_month_raise.append(eval(c) if c != '' else 0)
                    elif ix == 10:
                        six_month_raise.append(eval(c) if c != '' else 0)
                    elif ix == 11:
                        one_year_raise.append(eval(c) if c != '' else 0)
                    elif ix == 12:
                        two_year_raise.append(eval(c) if c != '' else 0)
                    elif ix == 13:
                        three_year_raise.append(eval(c) if c != '' else 0)
                    elif ix == 14:
                        this_year_raise.append(eval(c) if c != '' else 0)
                    elif ix == 15:
                        running_raise.append(eval(c) if c != '' else 0)
        import time

        print('已经完成第{}页'.format(page + 1))
        time.sleep(1)
    Dataframe_func = pd.DataFrame(
        {'code': code, 'name': name, 'net_value': net_value, 'accumulate_net': accumulated_net, 'day_raise': day_raise, \
         'week_raise': week_raise, 'one_month_raise': one_month_raise, 'three_month_raise': three_year_raise,
         'six_month_raise': six_month_raise, 'one_year_raise': one_year_raise, 'two_year_raise': two_year_raise,
         'three_year_raise': three_year_raise, 'this_year_raise': this_year_raise, 'running_raise': running_raise, })
    return Dataframe_func

if __name__ == "__main__":
    func_data = func_spider(3)
    print(func_data.iloc[:,2:].mean())
    plt.hist2d(x = func_data.this_year_raise.values,y = func_data.running_raise,bins = 20,label = 'this_year_raise')
    plt.legend(loc = 'best')
    plt.show()
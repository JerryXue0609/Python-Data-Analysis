import requests
import json
import time
import pandas as pd

#获取每一页数据
def get_one_page(url):
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.text
    return None

#解析每一页数据
def parse_one_page(html):

    data = json.loads(html)['cmts']#获取评论内容
    for item in data:
        yield{
        'date':item['time'].split(' ')[0],
        'nickname':item['nickName'],
        'city':item['cityName'],
        'rate':item['score'],
        'conment':item['content']
        }

#保存到文本文档中
def save_to_CSV():
    t1 = time.time()
    data = [] #获取所有数据
    for i in range(1,501):
        url = 'http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        for item in parse_one_page(html):
            if item not in data:
                data.append(item)
    conment = pd.DataFrame(data, columns=['nickname', 'city', 'conment', 'rate', 'date'])
    conment.to_csv('./maoyan_conment.csv', index=False, encoding='UTF-8')

    print('total use: %s 秒' % (time.time()-t1))
if __name__ == '__main__':
    save_to_CSV()
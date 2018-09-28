import requests
import time
import json

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
def save_to_txt():
    for i in range(1,1001):
        print("开始保存第%d页" % i)
        url = 'http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset=' + str(i)
        html = get_one_page(url)
        f = open('./我不是药神.txt', 'a', encoding='utf-8')
        for item in parse_one_page(html):
                f.write(item['date'] + ','+item['nickname'] +','+item['city'] +','
                    +str(item['rate']) +',' +item['conment']+'\n')

#去重重复的评论内容
def delete_repeat(old,new):
    oldfile = open(old,'r',encoding='utf-8')
    newfile = open(new,'w',encoding='utf-8')
    content_list = oldfile.readlines() #获取所有评论数据集
    content_alread = [] #存储去重后的评论数据集

    for line in content_list:
        if line not in content_alread:
            newfile.write(line+'\n')
            content_alread.append(line)

if __name__ == '__main__':
    save_to_txt()
    delete_repeat(r'./我不是药神.txt',r'./我不是药神_new.txt')
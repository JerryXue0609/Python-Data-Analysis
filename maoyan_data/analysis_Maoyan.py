from wordcloud import WordCloud,STOPWORDS
import pandas as pd 
import jieba
import matplotlib.pyplot as plt
from pyecharts import Geo,Style,Line,Bar,Overlap

f = open('./initData/我不是药神_new.txt',encoding='utf-8')
data = pd.read_csv(f,sep=',',header=None,encoding='utf-8',names=['date','nickname','city','rate','comment'])

city = data.groupby(['city'])
rate_group = city['rate']
city_com = city['rate'].agg(['mean','count'])
#print(city_com)
city_com.reset_index(inplace=True)
city_com['mean'] = round(city_com['mean'],2) #保留两位小数

#热力图分析
data_map = [(city_com['city'][i],city_com['count'][i]) for i in range(0,city_com.shape[0])]
#print(data_map)
style = Style(title_color="#fff",title_pos = "center",
            width = 1000,height = 600,background_color = "#404a59")

geo = Geo("《我不是药神》各城市观影人数分析","data from MAOYAN",**style.init_style)


while True:
    try:
        attr,val = geo.cast(data_map)
        geo.add("",attr,val,visual_range=[0,20],
                visual_text_color="#fff",symbol_size=20,
                is_visualmap=True,is_piecewise=True,
                visual_split_number=4)
    except ValueError as e:
        e = str(e)
        e = e.split("No coordinate is specified for ")[1]#获取不支持的城市名
        for i in range(0,len(data_map)):
            if e in data_map[i]:
                data_map.pop(i)
                break
    else:
        break
geo.show_config()
geo.render("./result/geo.html")

#折线+柱图分析

city_main = city_com.sort_values('count',ascending=False)[0:20]
#print(city_main)
attr = city_main['city']
v1 = city_main['count']
v2 = city_main['mean']
#print(attr,v1,v2)
line = Line("主要城市评分")
line.add("城市",attr,v2,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    is_splitline_show=False)

bar = Bar("主要城市评论数")
bar.add("城市",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('./result/主要城市评论数_平均分.html')


#词云分析
#分词

comment = jieba.cut(str(data['comment']),cut_all=False)
wl_space_split = " ".join(comment)

#导入背景图
backgroud_Image = plt.imread('./img/bj4.jpg')
stopwords = STOPWORDS.copy()
#print("STOPWORDS.copy()",help(STOPWORDS.copy()))


wc = WordCloud(width=1200,height=900,background_color='white',
    mask=backgroud_Image,font_path="./font/simhei.ttf",
    stopwords=stopwords,max_font_size=300,
    random_state=50)

wc.generate_from_text(wl_space_split)

plt.imshow(wc)
plt.axis('off')#不显示坐标轴  
#plt.show()
wc.to_file(r'./result/wordcloud_result.jpg')
print("处理完成")

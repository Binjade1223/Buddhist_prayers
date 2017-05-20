# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

#import module
import requests
from bs4 import BeautifulSoup
import time

#params
url = 'https://docs.google.com/spreadsheets/d/19Im7f2Q25eeUurqyMNosQMSsWeCHLhE9wxD1UBsgQMk/pubhtml?gid=955074027&single=true'

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
index = 16
data = []

#parser
for item in soup.select('.waffle'):
        while (index < len(item.select('td'))):
                every_one_data = []
                if time.strftime("%Y/") + str(int(time.strftime("%m")))+"/" +str(int(time.strftime("%d"))) in (item.select('td')[index].text):
                        for i in range(1,8):
                                every_one_data.append(item.select('td')[index + i].text)
                                i+=1
                        data.append( every_one_data )
                index += 8

#data_managing
article_data = ["-誦: ", "-持或稱頌: ", "-讀誦: ", "-"]
transferring_data = []

for item in data:
        for i in range(4):
                split_item = item[i+2].split(",")
                for j in range(len(split_item)):
                        if split_item[j] not in article_data[i]:
                                article_data[i]+= split_item[j]+", "
                        j+=1
                i+=1

for item in data:
        transferring_data.append(item[6])

#file_writing
f = open("Buddhism.txt","w+")

f.write("迴向: "+ time.strftime("%Y/%m/%d")+"\n")
f.write("文殊師利勇猛智"+"\n")
f.write("普賢慧行亦復然"+"\n")
f.write("我今迴向諸善根"+"\n")
f.write("隨彼一切常修學"+"\n")
f.write("三世諸佛所稱歎"+"\n")
f.write("如是最勝諸大願"+"\n")
f.write("我今迴向諸善根"+"\n")
f.write("為得普賢殊勝行"+"\n")
f.write(" "+"\n")
f.write("願將大家誠心"+"\n")

for i in range(4):
        f.write(article_data[i]+"\n")
        i+=1

f.write("以及大眾於日常生活中密行.說好話.做好事.存好心 ...之功德"+"\n")
f.write(" "+"\n")
f.write("迴向全球少些戰爭,人民多些幸福;社會多些溫暖,環境少些汙染.願你我每天都能如晨曦般,成就學業點亮這世界!"+"\n")
f.write(" "+"\n")

f.write("並迴向"+"\n")

f.write("------------------"+"\n")

for item in transferring_data:
        i = 1
        if item != "":
                f.write(str(i)+". 迴向 "+ item +"\n")
        i+=1

f.write("------------------"+"\n")

f.close()

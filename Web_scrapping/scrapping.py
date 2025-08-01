import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import json

current_datetime = datetime.now()
yr = current_datetime.year
mon = current_datetime.month
day = current_datetime.day
my_list = []
page = 1

while page<=2:
    base_url = f'https://news.ycombinator.com/?p={page}'
    req = requests.get(base_url)
    soup = BeautifulSoup(req.text,'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    def getting_top_hn(links,subtext):
        for indx,item in enumerate(links):
            title = item.find_next('a').get_text()
            link = item.find_next('a').get('href')
            point = subtext[indx].select('.score')
            if len(point):
                vote = int(point[0].get_text().replace(" points",""))
                if vote > 99:
                    my_list.append({'Title' : title,'link' : link , 'Points' : vote})
    getting_top_hn(links,subtext)

    page+=1
    time.sleep(1)

my_list.sort(key= lambda k:k['Points'], reverse= True)
with open(f'News[{day}-{mon}-{yr}].json', 'w', encoding='utf-8') as jsonfile:
    json.dump(my_list, jsonfile, ensure_ascii=False, indent=4)



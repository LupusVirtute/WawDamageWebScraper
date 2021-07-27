from bs4 import BeautifulSoup
from lxml import html
import requests

URL = 'https://callofduty.fandom.com/wiki/Upgraded_weapons/World_at_War'



path = '//table[@class="wikitable"][$i]/tbody/tr[3]/td[$j]/text()'
namePath = '//table[@class="wikitable"][$i]/tbody/tr[1]/th[$j]/text()'

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})
  
webpage = requests.get(URL, headers=HEADERS)
tree = html.fromstring(webpage.content)
sourceFile = open('output.txt', 'w')
for i in range(1,27):
    betterPath = path.replace('$i',str(i)).replace('$j',str(2))
    betterNamePath = namePath.replace('$i',str(i)).replace('$j',str(2))
    print(tree.xpath(betterNamePath)[0] + ":",file=sourceFile)
    print(tree.xpath(betterPath)[0],file=sourceFile)
sourceFile.close()

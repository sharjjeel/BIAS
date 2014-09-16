import sys
sys.path.insert(0, 'feedparser-5.1.3/feedparser')
import feedparser
import re
import operator
import json

fox = 'http://feeds.foxnews.com/foxnews/most-popular?format=xml'

foxFeed = feedparser.parse(fox)

dic = {}

def putter(dictionary, line, weight):
    line = re.sub('[^0-9a-zA-Z ]+', '', line)
    for a in line.split(" "):
        if len(a) > 3:
            if a in dictionary:
                dictionary[a] += weight;
            else:
                dictionary[a] = weight;

i = 0
for article in foxFeed["items"]:
    dic_new = {}
    putter(dic_new, article["title"], 2)
    sorted_dic = sorted(dic_new.iteritems(), key = operator.itemgetter(1), reverse = True)
    
    dic[i] = (sorted_dic, article["link"], article["title"])
    i+=1

json.dump(dic, open("fox.json", 'w'))


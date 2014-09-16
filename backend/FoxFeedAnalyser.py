import sys
sys.path.insert(0, 'feedparser-5.1.3/feedparser')
import feedparser
import re
import operator
import json
# First feed to read
fox = 'http://feeds.foxnews.com/foxnews/most-popular?format=xml'
# Parse using feedparser(open source)
foxFeed = feedparser.parse(fox)

dic = {}
# This function simply replaces all non aplhanumerics into empty space and then
# counts the occurances of each word
def putter(dictionary, line, weight):
    line = re.sub('[^0-9a-zA-Z ]+', '', line)
    for a in line.split(" "):
        if len(a) > 3:
            if a in dictionary:
                dictionary[a] += weight;
            else:
                dictionary[a] = weight;


i = 0
# goes through each article and finds the keywords using putter
# At the moment only uses title of the article, but can use other attributes
# Sorts the keywords based the importance of the keyword
for article in foxFeed["items"]:
    dic_new = {}
    putter(dic_new, article["title"], 2)
    sorted_dic = sorted(dic_new.iteritems(), key = operator.itemgetter(1), reverse = True)
    
    dic[i] = (sorted_dic, article["link"], article["title"])
    i+=1

# dumps in json format
json.dump(dic, open("fox.json", 'w'))


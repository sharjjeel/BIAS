import sys
sys.path.insert(0, 'feedparser-5.1.3/feedparser')
import feedparser

fox = "http://feeds.foxnews.com/foxnews/latest"
cnn = 'http://rss.cnn.com/rss/cnn_topstories.rss'
rt = 'http://rt.com/rss/'
spiegal = 'http://www.spiegel.de/international/index.rss'

dic_total = {};
rtfeed = feedparser.parse(rt)
cnnfeed = feedparser.parse(cnn)
foxfeed = feedparser.parse(fox)
spiegalfeed = feedparser.parse(spiegal)

def counter(line):
    for a in line.split(" "):
        if a in dic_total:
            dic_total[a] = dic_total[a] + 1
        else: 
            dic_total[a] = 1
for item in rtfeed["items"]:
    counter(item["title"])
for item in cnnfeed["items"]:
    counter(item["title"])
for item in foxfeed["items"]:
    counter(item["title"])
for item in spiegalfeed["items"]:
    counter(item["title"])

print dic_total

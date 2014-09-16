import json
import operator
# loads the json files
rt = json.load(open("rt.json"))
fox = json.load(open("fox.json"))
# compares lists of keywords to see how much articles match
def comp(keywords1, keywords2):
    c = 0
    for (word1, weight1) in keywords1:
        for (word2, weight2) in keywords2:
            if word1 == word2:
                c+= weight1 + weight2
    return c

compared_dic = {}
# crosses the articles and calls function comp() to add a number to each
# pair of articles. Makes sure the compared is not 0.
for rt_article in rt:
    for fox_article in fox:
        rt_keywords = rt[rt_article][0]
        fox_keywords = fox[fox_article][0]
        compared_int = comp(rt_keywords, fox_keywords)
        if compared_int != 0:
            compared_dic[(rt_article, fox_article)] = compared_int

# sorts based on how close articles are. The closest articles are at the top

sorted_dic = sorted(compared_dic.iteritems(), key = operator.itemgetter(1), reverse = True)

output_dic = {}
i = 0

occured_rt_articles = []
occured_fox_articles = []

# makes sure that articles are only shown once(only shown with their highest matched article)
# gets the title, link and outputs as dictionary.
for tup in sorted_dic:
    pair = tup[0]
    if pair[0] in occured_rt_articles:
        continue
    if pair[1] in occured_fox_articles:
        continue
    occured_rt_articles.append(pair[0])
    occured_fox_articles.append(pair[1])

    rt_link = rt[pair[0]][1]
    fox_link = fox[pair[1]][1]
    rt_title = rt[pair[0]][2]
    fox_title = fox[pair[1]][2]
    output_dic[i] = (rt_title, rt_link, fox_title, fox_link)
    i += 1

print output_dic
# dumps the output as JSON
json.dump(output_dic, open("similar.json", 'w'))

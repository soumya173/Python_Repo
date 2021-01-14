import requests
import json

url = "https://newsapi.org/v1/articles?source=the-hindu&sortBy=latest&apiKey=0df41ea97ffa4e2abee1a55636aed265"

#Read data from a file
def readData(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

#Load JSON data from URL
def readFromUrl(url):
    data = requests.get(url)
    jsonString = data.text
    jsonDict = json.loads(jsonString)
    articles = jsonDict['articles']

    return articles

#Write data to a file
def writeData(data, filename):
    """
    with open(filename, "a+") as f:
        json.dump(data, f)
        print("Written: " + data)
    """
    with open(filename, 'a') as f:
        str = json.dumps(data).replace('{', ',', 1)
        f.seek(-2, 2)
        f.write(str)

#Removes url and urlToImage from data
def cleanData(data):
    for item in data:
        del item['url']
        del item['urlToImage']
    return data

newsData = readFromUrl(url)
newsDataCleaned = cleanData(newsData)

for item in newsDataCleaned:
    writeData(item, "data.json")

# articles = newsData['articles']

# print("Latest articles are:" + "\n" + "-"*40)
# for article in newsData['articles']:
#     writeData(article, "data.json")
# del newsData['url']


print(type(newsDataCleaned))

# print(newsData)
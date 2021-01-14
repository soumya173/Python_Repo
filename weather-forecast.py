from bs4 import *
import requests

page = requests.get("http://www.accuweather.com/en/in/haldia/196593/weather-forecast/196593")
soup = BeautifulSoup(page.text, "html.parser")

link = soup.find('li', {'class':'day current first cl'})

classInfo = link.find('div', {'class':'info'})

classTemp = classInfo.find('span',{'class':'large-temp'})
degLabel = classInfo.find('span', {'class':'temp-label'})
descLabel = classInfo.find('span', {'class':'cond'})

temp = classTemp.contents
tempLabel = degLabel.contents
desc = descLabel.contents

print("Weather reports of Haldia")
print("Current Temperature: "+temp[0]+tempLabel[0])
print("Weather type: "+desc[0])

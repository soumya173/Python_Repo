from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import os
import datetime
from WindowsBalloonTip import WindowsBalloonTip
import time

# pip3 install urllib3
# pip install beautifulsoup4
# pip install pypiwin32

def donwloadDesignOfTheDay(link):
	page = urlopen(link)
	soup = BeautifulSoup(page.read(), "html.parser")
	dateStr = datetime.date.today()

	posts = soup.findAll("div", {"class": "col-sm-4 col-xs-6 _dP"})
	# col-sm-4 col-xs-6 _dK
	# col-sm-4 col-xs-6 _d0
	# col-sm-4 col-xs-6 _it
	# col-sm-4 col-xs-6 _dP

	# print(posts)

	titles = []
	imageLinks = []

	for post in posts:
		image = post.find("img")
		title = post.find("div", {"class": "_dX"}).text
		# _dS
		# _d8
		# _iB
		# _dX

		# print(image)

		if title not in titles:
			titles.append(title)
			imageLinks.append(image['src'])

	if not os.path.isdir(os.path.join("D:\\Codes\\Python\\BewakoofUpdates\\Downloads\\" , str(dateStr))):
			os.mkdir(os.path.join("D:\\Codes\\Python\\BewakoofUpdates\\Downloads\\" , str(dateStr)))
			print(str(dateStr) , "Directory created.")

	for i in range(len(imageLinks)):
		filename = os.path.join("D:\\Codes\\Python\\BewakoofUpdates\\Downloads\\" , str(dateStr), imageLinks[i].split("/")[-1])

		print("Downloading : " , str(imageLinks[i].split("/")[-1]))
		urlretrieve(imageLinks[i], filename)

	print("Download Completed.")
	notifTitle = "Today's Design of the Day."
	notifMsg = "Check it now @ \\Downloads\\" + str(dateStr) + "\\"
	print(notifMsg)
	WindowsBalloonTip(notifTitle, notifMsg)

link = "https://www.bewakoof.com/design-of-the-day"
donwloadDesignOfTheDay(link)
# time.sleep(10)
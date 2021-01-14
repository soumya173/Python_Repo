from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from random import shuffle
from datetime import datetime
import os
import ctypes
import struct
import time

# https://quotefancy.com/motivational-quotes
# D:\Codes\Python\ChangeWallpaper

def downloadWallpapers(dirPath):
	link = "https://quotefancy.com/motivational-quotes"

	page = urlopen(link)
	soup = BeautifulSoup(page.read(), "html.parser")

	posts = soup.findAll("div", {"class": "wallpaper scrollable"})

	links = []

	for post in posts:
		postLink = post.find("img")
		temp = postLink.get("data-original", "")
		if temp != "":
			links.append(temp)

	for link in links:
		filename = link.split("/")[-1]
		downloadPath = os.path.join(dirPath, filename)
		print("Downloading : " + filename)
		urlretrieve(link, downloadPath)

	print("Download Complete.")


def getFiles(mypath):
	onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

	filePaths = []
	for file in onlyfiles:
		filePaths.append(os.path.join(mypath, file))

	return filePaths

downloadWallpapers("D:\\Codes\\Python\\ChangeWallpaper\\Downloads\\")

files = getFiles("D:\\Codes\\Python\\ChangeWallpaper\\Downloads\\")
index = 0;
length = len(files)
shuffle(files)

minute = 15
flag = False

print("#"*80)
print("Wally started...")
print("\tWally will change your wallpaper in every " + str(minute) + " minutes.")
print("#"*80)

while True:
	curTime = datetime.now().time()
	timeFields = str(curTime).split(":")
	hourField = timeFields[0]

	if flag == True and hourField >= 9:
		flag = False
		print("Good Morning. Wally is ready to work...")

	if hourField == 19:
		flag = True
		print("Good Night. See ya tomorrow...")
		time.sleep(14*60*60)

	SPI_SETDESKWALLPAPER = 20
	imgNo = index % length
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, files[imgNo], 0)
	index += 1
	print("="*50)
	print("Last Changed at : " + str(curTime))
	time.sleep(minute*60)
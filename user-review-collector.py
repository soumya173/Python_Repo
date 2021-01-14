from bs4 import BeautifulSoup

import os
import re
import json
import unicodedata
import urllib2 as fetch

print "Processing..."

"""	 ### Pages to crawl ###
--Amul Butter-24-http://www.mouthshut.com/product-reviews/Amul-Butter-reviews-925036304-page-
--Cadbury Dairy Milk Silk-26-http://www.mouthshut.com/product-reviews/Cadbury-Dairy-Milk-Silk-reviews-925602369-page-
--Cadbury Dairymilk-13-http://www.mouthshut.com/product-reviews/Cadbury-Dairymilk-reviews-925040023-page-
--Nestle KitKat-12-http://www.mouthshut.com/product-reviews/Nestle-KitKat-reviews-925039961-page-
--Kinder Joy-9-http://www.mouthshut.com/product-reviews/Kinder-Joy-reviews-925104232-page-
--Cadbury Dairy Milk Bubbly-8-http://www.mouthshut.com/product-reviews/Cadbury-Dairy-Milk-Bubbly-reviews-925763174-page-
--Amul Dark Chocolate-8-http://www.mouthshut.com/product-reviews/Amul-Dark-Chocolate-reviews-925759702-page-
--Cadbury Bournville Fine Dark Chocolate-6-http://www.mouthshut.com/product-reviews/Cadbury-Bournville-Fine-Dark-Chocolate-reviews-925616039-page-
--Cadbury Five Star-6-http://www.mouthshut.com/product-reviews/Cadbury-Five-Star-reviews-925042722-page-
--Goldflake-8-http://www.mouthshut.com/product-reviews/Goldflake-reviews-925054034-page-
--Goldflake Lights-5-http://www.mouthshut.com/product-reviews/Goldflake-Lights-reviews-925054035-page-
--Patanjali Cow Desi Ghee-12-http://www.mouthshut.com/product-reviews/Patanjali-Cow-Desi-Ghee-reviews-925740762-page-
--Amul Ghee-8-http://www.mouthshut.com/product-reviews/Amul-Ghee-reviews-925627319-page-
--Saffola-7-http://www.mouthshut.com/product-reviews/Saffola-reviews-925041061-page-
--Amul Ice Cream-13-http://www.mouthshut.com/product-reviews/Amul-Ice-Cream-reviews-925062707-page-
--Kwality Walls Ice Cream-6-http://www.mouthshut.com/product-reviews/Kwality-Walls-Ice-Cream-reviews-925047460-page-
--Kwality Wall's Cornetto-5-http://www.mouthshut.com/product-reviews/Kwality-Wall-s-Cornetto-reviews-925731451-page-
--Godrej Real Good Chicken-4-http://www.mouthshut.com/product-reviews/Godrej-Real-Good-Chicken-reviews-925046855-page-
--Suguna Chicken-2-http://www.mouthshut.com/product-reviews/Suguna-Chicken-reviews-925051936-page-
--Venky's Meat-1-http://www.mouthshut.com/product-reviews/Venky-s-Meat-reviews-925036314-page-
--Priya Pickles-6-http://www.mouthshut.com/product-reviews/Priya-Pickles-reviews-925037919-page-
--Patanjali Amla Pickle-4-http://www.mouthshut.com/product-reviews/Patanjali-Amla-Pickle-reviews-925813949-page-
--Mother's Recipe Pickles-2-http://www.mouthshut.com/product-reviews/Mother-s-Recipe-Pickles-reviews-925040890-page-
--Kissan Sauce-5-http://www.mouthshut.com/product-reviews/Kissan-Sauce-reviews-925036310-page-
--Maggi Sauce Rich Tomato-4-http://www.mouthshut.com/product-reviews/Maggi-Sauce-Rich-Tomato-reviews-925731223-page-
--Nutella-3-http://www.mouthshut.com/product-reviews/Nutella-reviews-925738008-page-
--Maggi Sauce Hot & Sweet-3-http://www.mouthshut.com/product-reviews/Maggi-Sauce-Hot-Sweet-reviews-925731221-page-
--Knorr Soup-12-http://www.mouthshut.com/product-reviews/Knorr-Soup-reviews-925038717-page-
--Maggi Soup-4-http://www.mouthshut.com/product-reviews/Maggi-Soup-reviews-925053308-page-
--Ching's Secret Beijing Hot Soup-2-http://www.mouthshut.com/product-reviews/Ching-s-Secret-Beijing-Hot-Soup-reviews-925627302-page-

"""

to_crawl = "http://www.mouthshut.com/product-reviews/Ching-s-Secret-Beijing-Hot-Soup-reviews-925627302-page-"
no_pages = 2
print "Pages process: ", str(no_pages)

for k in range(0,no_pages):
	print "Processing Web Page : ",str(k+1), " !"

	file_flag = 1
	prev_data, new_data = ([] for lis in range(2))
	url = to_crawl + str(k+1)
	response = fetch.urlopen(url)

	data = response.read()

	soup = BeautifulSoup(data, "html.parser")

	p_data = soup.find_all('div',attrs= {'class':'more reviewdata'})

	product_title = soup.find('h1', attrs= {'id':'prodTitle1'})
	product_title1 = product_title.find('a')
	dir_name = product_title1.contents

	urls = []
	for data in p_data:
		for url in data:
			try:
				match_url = re.search('http://www.mouthshut.com/review/',url['onclick'])
				if match_url:
					tokens = url['onclick'].split(',')
					urls.append(tokens[7].strip("'"))
			except:
				pass

	final_data = []
	final_user = []
	urls_len = len(urls)
	# eli_list = ['<p>','</p>','<p class="lnhgt">','<br/>','<ul>','</ul>','<li>','</li>']
	# eli_list = '|'.join(eli_list)
	pattern = re.compile('<.*?>')

	for i in range(0,urls_len):
		response = fetch.urlopen(urls[i])
		data = response.read()
		soup = BeautifulSoup(data, "html.parser")

		revw_data = soup.find_all('div',attrs= {'class':'user-review'})
		user_data = soup.find_all('div', attrs= {'class':'profile'})

		for data in revw_data:
			texts = data.find_all("p", attrs = {'class':'lnhgt'})
			text = re.sub(pattern, '', str(texts[0]))
			final_data.append(text.strip("\n"))

		for data in user_data:
			users_data = data.find_all("p", attrs = {'id':'ctl00_ctl00_ContentPlaceHolderFooter_ContentPlaceHolderBody_lnkRevName'})
			user = users_data[0].get_text().strip("\n")
			user = unicodedata.normalize('NFKD', user).encode('ascii','ignore')
			final_user.append(user)

	dictionary = dict(zip(final_user,final_data))
	new_data.append(dictionary)
	dir_name1 = "/home/soumya/Data Collector/" + str(dir_name[0])

	try:
		os.mkdir(dir_name1)
	except:
		pass

	try:
		with open(str(dir_name[0])+'/data.json') as data_file:
			prev_data.append(json.load(data_file))
	except:
		file_flag = 0

	file = open(str(dir_name[0])+'/data.json','w')


	if file_flag == 1:
		file.write(json.dumps(prev_data + new_data))
	elif file_flag == 0:
		file.write(json.dumps(new_data))

	file.close()

print("Processing Finished!")




"""
	try:
		with open('data.json') as data_file:
			prev_data.append(json.load(data_file))
	except:
		file_flag = 0
"""

"""
	for i in range(0,len(final_data)):
		print str(i+1),". ",final_user[i]," --> ",final_data[i],"\n"

	print "Processing Completed Web Page : ",str(k+1), " !"
"""

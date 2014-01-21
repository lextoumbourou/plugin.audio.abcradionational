import requests
from BeautifulSoup import BeautifulSoup

def get_podcasts():
	page = requests.get("http://www.abc.net.au/radionational/podcasts")
	soup = BeautifulSoup(page.text)
	podcasts = soup.findAll('a', 'ico-download')
	titles = soup.findAll('h3', 'title')
	
	
	output = []
	for i in range(len(titles)):
		url = podcasts[i]['href']
		title = titles[i].text
		output.append({'url': url, "title": title})
	return  output 



	



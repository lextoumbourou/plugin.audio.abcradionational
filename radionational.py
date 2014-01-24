import requests
from BeautifulSoup import BeautifulSoup
import re

ABC_URL= "http://abc.net.au/radionational"

    #returns the menu categories
def menu_items():
    urls = [ABC_URL, "{0}/program".format(ABC_URL), "{0}/subjects".format(ABC_URL)]
    titles = ["Just In", "Programs", "Subjects"]
    output = []
    for i in range(len(urls)):
        title = titles[i]
        url = urls[i]
        output.append({'title':title, 'url': url})
    return output

    #returns the podcast urls and titles
def get_podcasts(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll('a', 'ico-download')
    titles = soup.findAll('h3', 'title')
    output = []
    for i in range(len(titles)):
		url = urls[i]['href']
		title = titles[i].text
		output.append({'url': url, 'title': title})
    return output
#get_podcasts("http://abc.net.au/radionational/podcasts")


 #returns the subject items from a url
def get_programs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll(href=re.compile("/radionational/programs/"))
    # use soup to extract text from href tags
    output = []
    for i in range(len(urls)):
        url = urls[i]['href']
        title = urls[i].text
        output.append({'url': url, 'title': title})
    return output


def define_program_url(url):
    programs = get_programs(url)
    output = []
    for program in programs:
        url = program['url']
        title = program['title']
        final = "http://www.abc.net.au" + url
        output.append({'url': final, 'title': title})
    return output



	



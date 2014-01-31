import requests
from BeautifulSoup import BeautifulSoup
import re

ABC_URL = "http://abc.net.au/radionational"


def get_podcasts(url_id):
    """
    Return playable podcasts links from ABC website
    """
    url = ABC_URL + url_id
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
    

def get_programs(url_id):
    """
    Return program info from ABC website
    """
    url = ABC_URL + url_id
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll(href=re.compile("/radionational/programs/"))
    programs = []
    for i in range(len(urls)):
        path = urls[i]['href']
        path_final = "http://www.abc.net.au" + path
        title = urls[i].text
    programs.append({'url': path_final, 'title': title})
    program_final = programs[40:-1]

    return program_final


def get_subjects(url_id):
    """
    Return subject info from ABC website
    """
    url = ABC_URL + url_id
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    urls = soup.findAll(href=re.compile("/radionational/subjects/"))
    programs = []
    for i in range(len(urls)):
        path = urls[i]['href']
        path_final = "http://www.abc.net.au" + path
        title = urls[i].text
    programs.append({'url': path_final, 'title': title})
    programs_final = programs[10:-1]

    return programs_final

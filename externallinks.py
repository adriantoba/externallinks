from bs4 import BeautifulSoup
import re
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def linkExtractor(url):

    opener = AppURLopener()

    resp = opener.open(url)

    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser" )

    a = []

    for link in soup.find_all('a', attrs={'href': re.compile("^http://")}): # only for the external links
    
    #for link in soup.find_all('a', href=True):    #for all the links
        
       a.append(link['href'])

    return a

    
print('\n'.join(map(str,linkExtractor("http://iasiexpert.ro/casa-si-gradina"))))










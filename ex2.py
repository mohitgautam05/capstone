import urllib2
from bs4 import BeautifulSoup

fish_url = "http://www.jeevanksh.com"
page = urllib2.urlopen(fish_url)
html_doc = page.read()
soup = BeautifulSoup(html_doc)

print(soup.prettify())
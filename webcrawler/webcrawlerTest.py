from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://xxx.test.com' ///URL 변경해야 한다.
response = urlopen(url)
plain_text = response.read()
soup = BeautifulSoup(plain_text, 'html.parser')

list = soup.find('code')

print(list)

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://repos.tmonc.net/cgit/cgit.cgi/www.git/plain/SG/config/www/rpc.qa.php'
response = urlopen(url)
plain_text = response.read()
soup = BeautifulSoup(plain_text, 'html.parser')

list = soup.find('code')

print(list)
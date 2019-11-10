from bs4 import BeautifulSoup
url = "https://blog.csdn.net/qq_32220889/article/details/82829866"
soup = BeautifulSoup(url, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
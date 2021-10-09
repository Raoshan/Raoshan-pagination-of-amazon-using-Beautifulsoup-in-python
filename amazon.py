import requests
from bs4 import BeautifulSoup
session = requests.Session()
url = f'https://www.amazon.in/s?k=dslr+camera&ref=nb_sb_noss_2'
headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
def getdata(url):
    req = session.get(url, headers=headers).text
    soup = BeautifulSoup(req, 'html.parser')
    return soup

def getnextpage(soup):
    #   next_ = soup.select_one("li.a-last a")
    # if not next_:
    #     next_ = soup.select_one(".s-pagination-next")
    #     if not next_:
    #         return

    # return "https://www.amazon.in" + next_["href"]
    # this will return the next page URL
    pages = soup.select_one('li.a-last a')
    if not pages:
        pages = soup.select_one("s-pagination")
        if not pages:
            return
    return "https://www.amazon.in" + pages["href"]

while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)



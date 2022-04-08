import requests
import dateparser
# import pymysql.cursors
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    l = soup.find('div', {'class': 'l-inline'}).text

    return  (l)


def send_telegram(text: str):
    TOKEN = None

    with open("token.txt") as f:
        TOKEN = f.read().strip()

    url = "https://api.telegram.org/bot"
    channel_id = "@ИМЯ_КАНАЛА"
    url += TOKEN
    method = url + "/sendMessage"

    r = requests.post(method, data={
        "chat_id": channel_id,
        "last_news": text
    })

    if r.status_code != 200:
        raise Exception("post_text error")

def main():
    url = 'https://vc.ru'
    send_telegram((get_data(get_html(url))))

if __name__ == '__main__':
    main()

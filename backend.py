import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip3 install beautifulsoup4')
    from bs4 import BeautifulSoup
import requests
from urllib import parse

sl = 'en'
tl = 'ko'
text = 'hello world'

link_google_translator = f'https://translate.google.co.kr/?hl=ko&sl={sl}&tl={tl}&text={parse.quote(text)}&op=translate'
link_papago = f'https://papago.naver.com/?sk={sl}&tk={tl}&hn=0&st={parse.quote(text)}'

res_google = requests.get(link_google_translator)
res_papago = requests.get(link_papago)

soup_google = BeautifulSoup(res_google.text, 'html.parser')
soup_papago = BeautifulSoup(res_papago.text, 'html.parser')

print(soup_papago.prettify())
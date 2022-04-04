import os
try:
    from bs4 import BeautifulSoup
except ImportError:
    os.system('pip3 install beautifulsoup4')
    from bs4 import BeautifulSoup
import requests
from urllib import parse

# https://translate.google.co.kr/?hl=ko&sl=en&tl=ko&text=hello%20world&op=translate
link_google_translator = 'https://translate.google.com/m?hl=en&sl=auto&tl=en&ie=UTF-8&prev=_m&q='
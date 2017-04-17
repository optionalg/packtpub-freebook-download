#https://www.packtpub.com/ebook_download/21051/pdf
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("https://www.packtpub.com/ebook_download/21051/pdf", auth=HTTPBasicAuth('develop.hermlon@t-online.de', 'useful_ebook'))
print(r.text)

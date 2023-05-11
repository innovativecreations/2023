import requests
from bs4 import BeautifulSoup
import lxml

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

r = requests.get("https://a.co/d/6Zdcukg", headers=headers)

soup = BeautifulSoup(r.content, "lxml")




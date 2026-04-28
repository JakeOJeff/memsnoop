from bs4 import BeautifulSoup
import requests

def scrapeTitles():
    pageToScrape = requests.get("https://orbitysws.vercel.app/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    titles = soup.find_all('h4', attrs={'class':'text-base'})

    for title in titles:
        print(title.text)

scrapeTitles()
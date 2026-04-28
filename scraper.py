from bs4 import BeautifulSoup
import requests

def scrapeBlogs():
    pageToScrape = requests.get("https://orbitysws.vercel.app/")
    soup = BeautifulSoup(pageToScrape, "html.parser")
    titles = soup.findAll('h4', attrs={'class':'text-base'})
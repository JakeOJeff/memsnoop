from bs4 import BeautifulSoup
import requests
import csv


with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"]) # uhh u can add other rows asw
    pageToScrape = requests.get("https://orbitysws.vercel.app/")
    soup = BeautifulSoup(pageToScrape.text, "html.parser")
    titles = soup.find_all('h4', attrs={'class':'text-base'})
    
    for title in titles:
        writer.writerow([title]) 
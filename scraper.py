from bs4 import BeautifulSoup
import requests
import csv

websites = []
with open("sites.csv", "r") as f:
    reader = csv.reader(f)
    for site in reader:
        websites.append(site[0])
        # print(site)
    
    for site in websites:
        print(site)

with open("books.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Title"]) # uhh u can add other rows asw

    for site in websites:

        pageToScrape = requests.get(site)
        soup = BeautifulSoup(pageToScrape.text, "html.parser")
        titles = soup.find_all('h4', attrs={'class':'text-base'})

        for title in titles:
            writer.writerow([title.text]) 


        # Playwright and scrapey
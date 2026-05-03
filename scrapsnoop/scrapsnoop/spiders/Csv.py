import scrapy
import csv
class CsvSpider(scrapy.Spider):
    name = "csv"

    def start_requests(self):
        with open("sites.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                yield scrapy.Request(url=row["url"], callback=self.parse)


    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "source_url":response.url,
            }
    
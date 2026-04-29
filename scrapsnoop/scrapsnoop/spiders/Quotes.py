import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()

            # dict
            yield {
                'Text': text,
                'Author': author,
                'Tags': tags
            }


#             >>> response.css('span.text').get()
# '<span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>'
# >>> response.css('span.text::text').get()
# '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'
# >>> response.css('small.author::text').get()
# 'Albert Einstein'
# >>> response.css('div.tags a.tag::text').get()
# 'change'
# >>> 
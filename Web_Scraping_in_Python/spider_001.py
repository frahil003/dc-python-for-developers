# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  async def start( self ):
    yield scrapy.Request(url = "https://example.com", callback = self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    text = response.css('h1::text').extract()
    for text in text:
      result_dict['H1'] = text
    
# Initialize the dictionary **outside** of the Spider class
result_dict = dict()

# Run the Spider
process = CrawlerProcess(settings = {"LOG_LEVEL": "WARNING"})
process.crawl(YourSpider)
process.start()

# Print a preview of courses
print(result_dict)
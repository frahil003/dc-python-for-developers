# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  async def start( self ):
    yield scrapy.Request(url = "https://franks-divecenter.de", callback = self.parse)

  # parse method    
  def parse(self, response):
    texts = response.css('p::text').getall()
    texts = [t.strip() for t in texts if t.strip()]
    result_dict['Text'] = texts

# Initialize the dictionary **outside** of the Spider class
result_dict = dict()

# Run the Spider
process = CrawlerProcess(settings = {"LOG_LEVEL": "WARNING"})
process.crawl(YourSpider)
process.start()

# Print a preview of courses
print(result_dict)
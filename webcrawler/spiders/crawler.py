# A Scrapy based Crawler for downloading web documents in html format- content crawling:– 
# Required: Initialize using seed URL/Domain, Max Pages, Max Depth

# Solution ==> This code defines a web crawler implemented using Scrapy, a Python framework for web scraping and crawling. The crawler is designed to download web documents in HTML format, enabling content crawling from the web.

# 1. **Initialization**: The crawler is initialized with the seed URL/domain, maximum pages to crawl, and maximum depth. 
# These parameters are provided by the user during initialization.

# 2. **File Management**: The crawler manages the storage of crawled URLs in a set and loads/saves them from/to a file named `crawled_urls.txt`. 
# This ensures that duplicate URLs are not crawled repeatedly.

# 3. **Starting Requests**: The `start_requests` method initiates the crawling process by sending requests to the start URLs provided by the user. 
# It specifies a callback function `parse` to handle the responses.

# 4. **Parsing Responses**: The `parse` method processes the response received from the server. 
# It checks if the maximum pages limit has been reached and if the URL has already been crawled. If the URL has been crawled before, it prompts the user to decide whether to crawl it again.

# 5. **Saving HTML Content**: If the URL is not a duplicate and the maximum pages limit has not been reached, the HTML content of the page is saved to a file in the `crawled_html` directory. 
# Each file is named based on the page number.

# 6. **Following Links**: The crawler follows links to other pages if the maximum depth has not been reached. 
# It extracts all links from the response and sends requests to follow them recursively.

# 7. **Closure**: The `closed` method is called when the spider is closed. 
# It logs a message indicating the closure of the crawler and the total number of pages crawled.

# Overall, this crawler provides a flexible and customizable solution for web document downloading and content crawling, allowing users to specify parameters and manage crawled URLs efficiently.""




import scrapy
import os

class WebCrawler(scrapy.Spider):
    name = 'webcrawler'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Get user input for seed URL/domain, maximum pages to crawl, and maximum depth
        self.start_urls = [input("Enter seed URL/domain: ")]
        self.max_pages = int(input("Enter maximum pages to crawl: "))
        self.max_depth = int(input("Enter maximum depth: "))
        self.pages_crawled = 0

        # Create a directory to save HTML files if it doesn't exist
        self.output_dir = 'crawled_html'
        os.makedirs(self.output_dir, exist_ok=True)

        # Initialize set to store crawled URLs
        self.crawled_urls = set()

        # Load crawled URLs from a file if it exists
        self.load_crawled_urls()

    def load_crawled_urls(self):
        """
        Method to load crawled URLs from a file if it exists.
        """
        filename = 'crawled_urls.txt'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.crawled_urls = set(f.read().splitlines())

    def save_crawled_urls(self):
        """
        Method to save crawled URLs to a file.
        """
        filename = 'crawled_urls.txt'
        with open(filename, 'w') as f:
            f.write('\n'.join(self.crawled_urls))

    def start_requests(self):
        """
        Method to start the crawling process by sending requests to the start URLs.
        """
        for url in self.start_urls:
            # Send requests to start URLs and specify the callback function to handle responses
            yield scrapy.Request(url=url, callback=self.parse, meta={'depth': 1})

    def parse(self, response):
        """
        Method to parse the response received from the server.
        """
        if self.pages_crawled >= self.max_pages:
            # Check if the maximum pages limit has been reached
            self.logger.info("Reached maximum pages limit. Crawling stopped.")
            return

        # Check if the URL has already been crawled
        if response.url in self.crawled_urls:
            crawl_again = input(f"The URL {response.url} has already been crawled. Do you want to crawl it again? (yes/no): ")
            if crawl_again.lower() != 'yes':
                self.logger.info(f"Skipping already crawled URL: {response.url}")
                return

        self.pages_crawled += 1

        # Extract HTML content from the response
        html_content = response.body.decode('utf-8')
        # Generate filename for the HTML file based on the page number
        filename = f'{self.output_dir}/page_{self.pages_crawled}.html'
        # Save the HTML content to a file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # Log a message indicating that the HTML content has been saved
        self.logger.info(f"Saved HTML content of {response.url} to {filename}")

        # Add the crawled URL to the set of crawled URLs
        self.crawled_urls.add(response.url)
        # Save crawled URLs to a file
        self.save_crawled_urls()

        # Follow links to other pages if the maximum depth has not been reached
        if response.meta['depth'] < self.max_depth:
            # Extract all links from the response and follow them
            for link in response.css('a::attr(href)').getall():
                # Send a request to follow the link and specify the callback function
                yield response.follow(link, self.parse, meta={'depth': response.meta['depth'] + 1})

    def closed(self, reason):
        """
        Method called when the spider is closed.
        """
        # Log a message indicating the closure of the crawler and the number of pages crawled
        self.logger.info(f"Crawler closed. Crawled {self.pages_crawled} pages.")

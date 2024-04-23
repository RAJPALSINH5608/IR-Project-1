# IR-Project
## Initial Setup 
1. Scrapy-Based Crawler:
Install Scrapy: pip install scrapy

2. Scikit-Learn Based Indexer:
Install Scikit-Learn: pip install scikit-learn
3. Flask-Based Processor:
Install Flask: pip install flask

## Abstract
This project introduces a versatile web crawling, indexing, and query processing system. Utilizing Scrapy for crawling, Scikit-Learn for indexing, and Flask for query processing, it enables efficient retrieval of web documents. Features include concurrent and distributed crawling, TF-IDF scoring, cosine similarity, and query validation. Optional enhancements include spelling correction/suggestion and query expansion. This system is designed to streamline web document retrieval and analysis tasks.


## Project Overview

Creating a reliable system that can rapidly crawl, index, and query web documents without requiring a web interface for human interaction was the goal of this project. The system uses a number of essential libraries and Python to automatically download HTML material from certain domains. It then uses sophisticated text processing algorithms to index the content for fast retrieval. In order to increase the accuracy of query results and broaden the system's capacity to handle a larger variety of document kinds and languages, future projects will investigate improved natural language processing features.
It allows for the effective retrieval of web documents by using Flask for query processing, Scikit-Learn for indexing, and Scrapy for crawling. TF-IDF scoring, cosine similarity, query validation, and concurrent and distributed crawling are among the features. 


---

## Design Overview

### Web Crawler Design:

- Initialization: Accepts seed URL/domain, maximum pages, and maximum depth parameters.
- Crawling Mechanism: Utilizes Scrapy framework for efficient web content retrieval.
- Concurrency: Supports concurrent crawling using AutoThrottle for optimal performance.
- Distributed Crawling: Integration with Scrapyd enables distributed crawling across multiple nodes.
- Document Format: Retrieves web documents in HTML format for further processing.

### Indexer Design:

- Inverted Index: Constructs an inverted index using Scikit-Learn, facilitating efficient search indexing.
- Document Representation: Utilizes TF-IDF scoring for document representation, capturing term frequency and inverse document frequency.
- Search Mechanism: Implements cosine similarity for calculating relevance scores, enabling accurate retrieval of relevant documents.


### Query Processor Design:

- Flask Integration: Built with Flask for handling free text queries in JSON format.
- Query Validation: Ensures query validity and performs error-checking to maintain accuracy.
- Ranking Mechanism: Ranks search results based on relevance scores calculated using TF-IDF and cosine similarity.
- The system boasts several capabilities to streamline web document retrieval and analysis. The crawler, equipped with auto-throttle functionality, efficiently manages request rates to maintain server-friendly interactions during the crawling process. In parallel, the indexer employs cosine similarity to score document relevance accurately. Additionally, the query processor seamlessly handles JSON requests, performing error checking and ranking responses to ensure optimal user experience. These modules interact through clearly defined interfaces, facilitating smooth data flow from the crawler to the indexer and enabling seamless querying of indexed results through the processor. This integrated approach combines data handling and processing functionalities, culminating in a user-friendly web service interface for effortless querying and analysis.
  

---

## Architecture 
Software Components:
- The system leverages Scrapy as its primary tool for web crawling, facilitating efficient retrieval of web content.
- BeautifulSoup is utilized for HTML parsing, enabling the extraction of relevant text content from crawled web pages.
- Scikit-Learn serves as the backbone for indexing, allowing the construction of an inverted index for efficient search operations.
- Flask is employed to develop the web interface, providing users with a seamless platform for interacting with the system.

Interfaces:
- Data seamlessly flows through the system via two main channels: files, including HTML and pickle files, and in-memory data structures represented as TF-IDF matrices.
- Files containing HTML documents and the inverted index in pickle format serve as persistent storage mediums for crawled content and search indexing information.
- In-memory TF-IDF matrices facilitate efficient representation and retrieval of document information during query processing.

Implementation:
- Each module is meticulously crafted as a distinct Python script, encapsulating specific functionalities tailored to its designated task.
- These individual modules are then seamlessly integrated, functioning harmoniously as a cohesive unit to deliver the desired service.
- This modular approach not only enhances maintainability but also enables scalability and flexibility in adapting to evolving requirements and system enhancements.

### Operation

- *Commands:* The system primarily operates through Python scripts, leveraging the Flask application as the primary interface for querying. Users interact with the system by executing predefined commands within the Python environment, allowing them to initiate crawling, perform indexing, and execute queries seamlessly.

- *Inputs:* The system accepts two main types of inputs: URLs and free-text queries. URLs are provided to initiate the crawling process, specifying the starting point for the web crawler to traverse and retrieve web documents. Free-text queries are utilized to retrieve specific documents or information from the indexed data. Users can input their queries through the Flask interface, enabling them to search for relevant documents based on their requirements.

- *Installation:* Setting up the system requires Python to be installed on the user's machine. Once Python is installed, users can utilize the pip package manager to install the necessary dependencies. These dependencies include libraries and frameworks such as Scrapy, NLTK, Scikit-Learn, and Flask, which are essential for various functionalities of the system. By installing these dependencies, users can ensure that the system functions smoothly and efficiently, ready to perform crawling, indexing, and query processing tasks.

### Conclusion:

- Results:
The system demonstrates remarkable efficiency and relevance in its ability to crawl, index, and query documents. It effectively retrieves, organizes, and presents information, showcasing its capability to fulfill user needs swiftly and accurately.

- Outputs:
The system generates various outputs, including HTML documents obtained through crawling, indexed files for efficient retrieval, and query results presented in JSON format. These outputs serve as valuable resources for users, enabling them to access relevant information in a structured and easily accessible manner.

- Caveats/Cautions:
While the system excels in its core functionalities, there are certain limitations and precautions to consider. Currently, the system is confined to predefined domains, which may restrict its applicability in broader contexts. Additionally, it lacks comprehensive error handling mechanisms tailored to real-world scenarios, which could impact its reliability and robustness in handling unexpected situations. Therefore, users should exercise caution and be aware of these limitations when utilizing the system for their specific needs.

## Data Sources:

- Data Source: The testing and setup procedures rely on data sourced from "Reddit," which can be accessed at (https://www.reddit.com/).
- Data Access: The retrieval of data is entirely automated through the crawler, removing the necessity for manual downloads or any form of manual intervention. This streamlines the testing and setup process, ensuring efficiency and accuracy in data retrieval.

## Test Cases:

- Framework:Testing procedures are executed utilizing Python's unittest framework, facilitating the implementation of modular tests for individual components within the system.

- Coverage:The range of test cases spans across multiple functionalities, ensuring thorough examination of elements such as confirming crawling depth, adhering to specified page count parameters, achieving precision in indexing operations, and validating the accuracy of query responses.
Documentation:

- Inline Comments: Incorporating inline comments within the codebase serves to elucidate usage intricacies and configuration specifics, thereby augmenting the readability and comprehensibility of the codebase for developers and collaborators.
- README Files: Comprehensive README files complement the codebase by furnishing supplementary documentation, furnishing insights into system utilization, setup procedures, and configuration directives, thereby facilitating seamless navigation and understanding of the project for users and contributors alike.

## Source Code

The system leverages a range of open-source Python libraries to empower its core functionalities, spanning web crawling, indexing, and query processing tasks. For instance, Scrapy, a widely-used framework, serves as the backbone for efficient web content retrieval. Additionally, Scikit-Learn plays a pivotal role in constructing an inverted index, enabling TF-IDF scoring and cosine similarity calculations for precise search indexing. Flask, another crucial component, provides the foundation for the query processing module, allowing seamless handling of free text queries in JSON format. These libraries, alongside others, collectively contribute to the system's robustness and flexibility, ensuring streamlined operations across the entire pipeline.

## Bibliography:

Bibliography:

[1] Scrapy Documentation. Retrieved from: https://scrapy.org/

[2] Flask Documentation. Retrieved from: https://flask.palletsprojects.com/en/3.0.x/installation/#python-version

[3] Butterfly - Ladybug Tools. Retrieved from: https://www.ladybug.tools/butterfly.html

[4] Topcoder. (n.d.). Building a Web Crawler in Python. Retrieved from: https://www.topcoder.com/thrive/articles/web-crawler-in-python

[5] Scikit-Learn Documentation: TfidfVectorizer. Retrieved from: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

# Web-Scraping-News-Article

#News Scraping Script
This Python script scrapes news articles from the Indian Express website's India section and stores them in a CSV file. It utilizes the requests library to fetch the HTML content of the webpage and the BeautifulSoup library to parse the HTML and extract relevant information such as headline, date, and article content.

#Features:
Scrapes news articles from the Indian Express website's India section.
Appends new articles to a CSV file, avoiding duplicates.
Provides error handling and logging for robustness.
#Requirements:
Python 3.x
requests library
BeautifulSoup library
pandas library
#Usage:
Clone the repository to your local machine.
Install the required libraries using pip install -r requirements.txt.
Run the script using python news_scraping.py.
#CSV File:
The scraped news articles are stored in a CSV file named news_every_hour.csv. The CSV file has three columns: Headline, Date, and Info.

#Contributing:
Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

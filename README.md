# LearningSelenium

This repository contains various Python scripts demonstrating the use of Selenium for web automation, element location strategies, and data extraction.

## Structure

- **collect.py**  
  Parses saved HTML files using BeautifulSoup to extract product titles, links, and prices, and stores them in a CSV file.

- **locating_single.py**  
  Demonstrates locating a single web element using different Selenium strategies like ID, name, class, etc.

- **locating_multiple.py**  
  Demonstrates locating multiple web elements using tag name, class name, XPath, and CSS selectors.

- **main.py**  
  Serves as the primary driver script to initialize Selenium, configure browser options, and run scraping routines.

- **project.py**  
  Contains a consolidated or advanced script for scraping or automation tasks using Selenium.

## Setup

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
````

3. Install dependencies:

```bash
   pip install -r requirements.txt
```

## Requirements

* Python 3.7+
* Google Chrome or another supported browser
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) matching your Chrome version
* `selenium`, `beautifulsoup4`, and `pandas`

## Output

* `data.csv`: Contains extracted product information like title, price, and link.

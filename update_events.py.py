import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def get_formated_date():
    """
    Returns today's date formatted as 'YYYY_Month_Day' without leading zeros in the day.
    """
    today_date = datetime.today()
    formatted_date = today_date.strftime("%Y_%B_%d").lstrip('0').replace('_0', '_')

    return formatted_date

def format_url(date):
    """
    Formats the given date into the structure of a Wikipedia 'Current Events' portal URL.
    """
    url = f'https://en.wikipedia.org/wiki/Portal:Current_events/{date}'
    return url

def get_html(url):
    """
    Retrieves the HTML content of a webpage given its URL.
    """
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to retrieve page: Status code {response.status_code}")
        print(url)
        return

    return response.content

def process_data(html):
    """
    Processes the HTML content of the Wikipedia page and extracts event information.

    Returns:
        A list of tuples containing the date, event text, and the first link related to the event.
    """
    soup = BeautifulSoup(html, 'html.parser')
    events = []
    div_element = soup.find('div', class_='current-events-content description')

    if div_element:
      for ul in div_element.find_all('ul'):
          for li in ul.find_all('li', recursive=False):
              event_text = li.text.strip()

              link = li.find('a', href=True)
              link_url = f"https://en.wikipedia.org{link['href']}" if link else 'No link available'

              events.append((datetime.today(), event_text, link_url))

    return events

def update_database():
    """
    Updates csv file with extracted data
    """
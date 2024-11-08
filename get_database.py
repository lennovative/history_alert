import requests
import csv
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from urllib.parse import urljoin


def fetch_day_html(day_title, WIKI_API_URL="https://en.wikipedia.org/w/api.php"):
    """
    Fetches HTML content for a given day (e.g., "January 1") from Wikipedia.
    """
    params = {
        "action": "parse",
        "page": day_title,
        "format": "json",
        "prop": "text",
        "redirects": True,
    }
    response = requests.get(WIKI_API_URL, params=params)
    response.raise_for_status()

    data = response.json()
    page = data["parse"]["text"]["*"]
    return page


def clean_text(text):
    result = re.sub(r'\[ \d+\ ]', '', text)
    result = result.replace(" ,", ",")
    return result.strip()


def parse_section(entry_type, section, day_title, BASE_WIKI_URL="https://en.wikipedia.org"):
    result = []
    for h3 in section.find_all_next(["h3", "h2"], limit=None):
        if h3.name == "h2":
            break
        ul = h3.find_next("ul")
        if ul:
            for li in ul.find_all("li"):
                text = li.get_text(separator=" ", strip=True)
                entry = tuple([v.strip() for v in text.split("–")])
                if not len(entry) == 2:
                    continue
                year, description = entry
                # Find all <a> tags within the <li> to get URLs
                links_all = [urljoin(BASE_WIKI_URL, a['href']) for a in li.find_all("a", href=True)]
                links = [v for v in links_all if v.split("/")[-1] != year and "#cite_note" not in v]

                result.append({
                    "day": day_title,
                    "year": year,
                    "type": entry_type,
                    "description": clean_text(description),
                    "links": links
                })
    return result


def parse_events_and_birthdays(day_title, html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    events = []
    birthdays = []

    events_section = soup.find("h2", id="Events")
    if events_section:
        events = parse_section("Event", events_section, day_title)

    births_section = soup.find("h2", id="Births")
    if births_section:
        birthdays = parse_section("Birthday", births_section, day_title)

    return events, birthdays


def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Year", "Type", "Description", "Links"])
        for entry in data:
            links_joined = " ".join(entry["links"]) if entry["links"] else ""
            writer.writerow([entry["day"], entry["year"], entry["type"], entry["description"], links_joined])


def main():
    # Fetches historical events and birthdays for each day of the year.
    start_date = datetime(2024, 1, 1)  # Any leap year
    all_data = []

    for i in range(366):
        current_date = start_date + timedelta(days=i)
        day_title = current_date.strftime("%B %d")  # Format like "January 1"

        try:
            print(f"Fetching data for {day_title}...")
            day_content = fetch_day_html(day_title)
            if day_content:
                events, birthdays = parse_events_and_birthdays(day_title, day_content)

            for event in events:
                all_data.append(event)
                print(event)

            for birthday in birthdays:
                all_data.append(birthday)
                print(birthday)

            if day_title == "December 31":
                break

            time.sleep(2)

        except Exception as e:
            print(f"Error fetching {day_title}: {e}")
            continue

    # Save all data to CSV
    print("Saving all data to CSV...")
    filename = "database.csv"
    save_to_csv(all_data, filename)
    print(f"Data saved to '{filename}'.")


if __name__ == "__main__":
    main()


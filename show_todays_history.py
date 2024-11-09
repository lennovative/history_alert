import csv
import random
from datetime import datetime

def load_data_by_date(filename):
    data_by_date = {}

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Date"]
            event_type = row["Type"]
            if date not in data_by_date:
                data_by_date[date] = {"Event": [], "Birthday": []}
            data_by_date[date][event_type].append(row)

    return data_by_date

def get_random_event_and_birthday_for_date(data_by_date, date):
    if date in data_by_date:
        events = data_by_date[date]["Event"]
        birthdays = data_by_date[date]["Birthday"]
        random_event = random.choice(events) if events else None
        random_birthday = random.choice(birthdays) if birthdays else None
        return random_event, random_birthday
    else:
        print(f"No data found for {date}.")
        return None, None

def display_results(date, event, birthday):
    print("HistoryAlarm\n")
    if event:
        print(f"{date}, {event['Year']} - {event['Description']} ({event['Links']})\n")
    else:
        print("No events available for today.")

    if birthday:
        print(f"{date}, {birthday['Year']} - Birthday of {birthday['Description']} ({birthday['Links']})\n")
    else:
        print("No birthdays available for today.")


def main():
    filename = "database.csv"
    data_by_date = load_data_by_date(filename)
    current_date = datetime.now().strftime("%B %d")
    event, birthday = get_random_event_and_birthday_for_date(data_by_date, current_date)
    display_results(current_date, event, birthday)


if __name__ == "__main__":
    main()


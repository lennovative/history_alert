import csv
import random
from datetime import datetime
import base64

def load_data_by_date(filename, blacklist):
    data_by_date = {}

    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            date = row["Date"]
            event_type = row["Type"]
            description = row["Description"].lower()

            if any(word in description for word in blacklist):
                continue

            if date not in data_by_date:
                data_by_date[date] = {"Event": [], "Birthday": []}
            data_by_date[date][event_type].append(row)

    return data_by_date



def load_blacklisted_words_from_binary(filepath='blacklisted_words.bin'):
    with open(filepath, 'rb') as file:
        encoded_data = file.read()

    decoded_data = base64.b64decode(encoded_data).decode('utf-8').split(',')
    return decoded_data


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
    print("\n")
    print("HistoryAlert\n")
    if event:
        print(f"{date}, {event['Year']} - {event['Description']} ({event['Links']})\n")
    else:
        print("No events available for today.")

    if birthday:
        print(f"{date}, {birthday['Year']} - Birthday of {birthday['Description']} ({birthday['Links']})\n")
    else:
        print("No birthdays available for today.")

def is_valid_date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, "%m-%d")
        return True
    except ValueError:
        return False

def main(current_date):
    blacklist = load_blacklisted_words_from_binary('blacklisted_words.bin')

    filename = "database.csv"
    data_by_date = load_data_by_date(filename, blacklist)

    if(current_date == False):
        current_date = datetime.now().strftime("%B %d")

    event, birthday = get_random_event_and_birthday_for_date(data_by_date, current_date)
    display_results(current_date, event, birthday)


if __name__ == "__main__":
    main()
    
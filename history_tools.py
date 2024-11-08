import pandas as pd
from colorama import Fore, Style

def fetch_historical_event(date='2024-11-08', csv_path='events.csv'):
    """
    Fetch a historical event for the provided date from a CSV file.

    Parameters:
    date (str): The date in the format 'YYYY-MM-DD'
    csv_path (str): The path to the CSV file containing historical events

    Returns:
    str: The historical event description or a message if no event is found.
    """
    # Read the CSV file
    try:
        df = pd.read_csv(csv_path)
        # Find the event for the provided date
        event_row = df[df['Date'] == date]
        if not event_row.empty:
            event = event_row.iloc[0]['Event']
            return f"{event}"
        else:
            return f"No event found for {date}."
    except FileNotFoundError:
        return "CSV file not found. Please check the file path."
    

def show_event():
    # Example function call and fancy output display
    event = fetch_historical_event()

    # Create a decorative border and styled output
    border = '=' * 50
    header = Fore.CYAN + '\n*** Historical Event of the Day ***\n' + Style.RESET_ALL

    print(Fore.YELLOW + border + Style.RESET_ALL)
    print(header)
    print(Fore.RED + event + Style.RESET_ALL)
    print(Fore.YELLOW + border + Style.RESET_ALL)

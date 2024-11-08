import argparse
import pyfiglet
from colorama import Fore, Style
import history_tools as his

def main():
    # Create a cool banner using pyfiglet
    banner = pyfiglet.figlet_format("HistoryAlert")
    print(Fore.CYAN + banner + Style.RESET_ALL)

    # Create the ArgumentParser object with a styled description
    parser = argparse.ArgumentParser(
        prog='HistoryAlert',
        description=Fore.YELLOW + 'Welcome to HistoryAlert! Discover historical events that happened on today\'s date or on a date you provide.' + Style.RESET_ALL,
        epilog=Fore.GREEN + 'Enjoy learning history one day at a time!' + Style.RESET_ALL
    )
    
    # Add argument for the user to provide a date
    parser.add_argument(
        '-d', '--date',
        type=str,
        help=Fore.MAGENTA + 'Specify a date in the format YYYY-MM-DD to get a historical event that happened on that day.' + Style.RESET_ALL
    )
    
    # Parse the arguments
    args = parser.parse_args()

    # Check if no arguments are provided
    if not any(vars(args).values()):
        parser.print_help()
        his.show_event()
    else:
        # Process the provided date if given
        if args.date:
            print(Fore.CYAN + f"Fetching historical event for the date: {args.date}" + Style.RESET_ALL)
        else:
            print(Fore.CYAN + "Fetching historical event for today." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

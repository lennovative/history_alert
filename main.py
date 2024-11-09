import argparse
import pyfiglet
from colorama import Fore, Style
import show_todays_history as tools
from datetime import datetime

def main():
    banner = pyfiglet.figlet_format("HistoryAlert")

    parser = argparse.ArgumentParser(
        prog='HistoryAlert',
        description=Fore.YELLOW + 'Welcome to HistoryAlert! Discover historical events that happened on today\'s date or on a date you provide.' + Style.RESET_ALL,
        epilog=Fore.GREEN + 'Enjoy learning history one day at a time!' + Style.RESET_ALL
    )
    
    parser.add_argument(
        '-d', '--date',
        type=str,
        help=Fore.MAGENTA + 'Specify a date in the format MM-DD to get a historical event that happened on that day.' + Style.RESET_ALL
    )

    parser.add_argument(
        '-s', '--silent',
        action='store_true',
        help='Run the program without the title banner.'
    )

    
    args = parser.parse_args()

    if not args.silent:
        print(Fore.CYAN + banner + Style.RESET_ALL)

    if not any(vars(args).values()):
        parser.print_help()
        tools.main(False)
    else:
        if args.date:
            try:
                date_obj = datetime.strptime(args.date, "%m-%d")
                tools.main(date_obj.strftime("%B %d"))
            except ValueError:
                print(Fore.RED + "Invalid date format. Please use MM-DD." + Style.RESET_ALL)
        else:
            tools.main(False)

if __name__ == "__main__":
    main()

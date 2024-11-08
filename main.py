import argparse

parser = argparse.ArgumentParser(
    prog='HistoryAlert',
    description='Welcome to Historical Event CLI! This app shows a historical event that happened on todays date or on a date you provide.',
    epilog='Enjoy learning history one day at a time!'
)

parser.add_argument(
    '-d', '--date',
    type=str,
    help='Specify a date in the format YYYY-MM-DD to get a historical event that happened on that day.'
)
    
args = parser.parse_args()

if not any(vars(args).values()):
    parser.print_help()
else:
    if args.date:
        print(f"Fetching historical event for the date: {args.date}")
    else:
        print("Fetching historical event for today.")
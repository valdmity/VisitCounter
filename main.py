import database as db
from datetime import datetime, timedelta
import argparse


d = {
"y": timedelta(days=365),
"m": timedelta(days=30),
"d": timedelta(days=1),
"a": timedelta(days=0)
}

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-b', '--browsers', action='store_true', default=False)
arg_parser.add_argument("-u", "--unique", action="store_true", default=False, \
    help="unique visits statistic")
arg_parser.add_argument("-y", "--year", action="store_true", default=False, \
    help="visits statistic for last year")
arg_parser.add_argument("-m", "--month", action="store_true", default=False, \
    help="visits statistic for last month")
arg_parser.add_argument("-d", "--day", action="store_true", default=False, \
    help="visits statistic for last day")


def get_result(args) -> str:
    if args.day:
        start_date = datetime.utcnow() - d['d']
    elif args.month:
        start_date = datetime.utcnow() - d['m']
    elif args.year:
        start_date = datetime.utcnow() - d['y']
    else:
        start_date = datetime.utcnow() - d['a']

    if args.browsers:
        stat = db.get_statistic_by_browsers(start_date)
        data = ''
        for value in stat:
            data += value[0] + ' - ' + value[1] + '\n'
        return data
    
    if args.unique:
        stat = db.get_values_count_visits_by_time(start_date)
        get_append_formatted_line = lambda v: v[0] + ' - ' + v[1] + '\n'
    else:
        stat = db.get_values_by_time(start_date)
        get_append_formatted_line = lambda v: v[0] + ' - ' + v[1] + ' - ' + v[2] + '\n'
        
    data = ''
    for value in stat:
        data += get_append_formatted_line(value)
    return data



if __name__ == '__main__':
    print(get_result(arg_parser.parse_args()))

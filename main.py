import database as db
from typing import Iterator
from datetime import datetime, timedelta
import sys


d = {
"y": timedelta(days=365),
"m": timedelta(days=30),
"d": timedelta(days=1),
"a": timedelta(days=0)
}


def get_result() -> str:
    if len(sys.argv) == 2 and sys.argv[1][1] == 'h':
        with open('commands.txt', 'r', encoding='utf-8') as f:
            help_text = f.read()
            return help_text

    if len(sys.argv) == 3:
        start_date = datetime.utcnow() - d[sys.argv[2][1]]
        stat = []
        if sys.argv[1][1] == 's':
            stat = db.get_values_by_time(start_date)
        elif sys.argv[1][1] == 'u':
            stat = db.get_values_count_visits_by_time(start_date)
        
        data = ''
        for value in stat:
            data += value[0] + ' - ' + value[1] + ' - ' + value[2] + '\n'
        return data
    
    return '400 BR'



if __name__ == '__main__':
    print(get_result())

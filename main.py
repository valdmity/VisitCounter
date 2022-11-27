import database as db
from typing import Iterator
import sys


def get_simple_visits_statistics() -> Iterator[tuple[str, str]]:
    '''
    return: pairs user_id and datetime 
    '''
    # TODO
    pass


def get_unique_visits_statistics() -> Iterator[tuple[str, str]]:
    '''
    return: pairs user_id and visits_count
    '''
    # TODO
    pass


def get_result() -> str:
    if len(sys.argv) == 2 and sys.argv[1][1] == 'h':
        with open('commands.txt', 'r', encoding='utf-8') as f:
            help_text = f.read()
            return help_text
    if len(sys.argv) == 3:
        if sys.argv[1][1] == 's':
            stat = get_simple_visits_statistics()
            # TODO
        elif sys.argv[1][1] == 'u':
            stat = get_unique_visits_statistics()
            # TODO
    return '400 BR'



if __name__ == '__main__':
    print(get_result())

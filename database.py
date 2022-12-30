from datetime import datetime, timedelta

DATABASE_FILE_PATH = "db.txt"
BROWSERS = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Opera']


def get_all_values() -> list[tuple[str, str, str]]:
    with open(DATABASE_FILE_PATH, 'r') as f:
        lines = f.readlines()
        
        if len(lines) == 0:
            return []

        items = []
        for line in lines:
            t = line.split(': ')
            a, b, c = t[0], t[1], t[2][:-1]
            items.append((a, b, c))
        return items


def get_values_by_time(start_date: datetime) -> list[tuple[str, str, str]]:
    values = get_all_values()
    if start_date + timedelta(days=0.5) > datetime.utcnow():
        return list(values)
    return [value for value in values
            if datetime.strptime(value[1], '%Y-%m-%d %H:%M:%S') > start_date]


def get_values_by_time_and_id(start_date: datetime, id: str) -> list[tuple[str, str, str]]:
    values = get_values_by_time(start_date)
    return [value for value in values if value[0] == id]


def get_statistic_by_browsers(time: datetime) -> list[tuple[str, str]]:
    stat = []
    all_stat = get_values_by_time(time)
    for browser in BROWSERS:
        stat.append((browser, str(len([s for s in all_stat if s[2] == browser]))))
    return stat


def get_all_ids() -> list[str]:
    values = get_all_values()
    return list(set([value[0] for value in values]))


def get_values_count_visits_by_time(start_date: datetime) -> list[tuple[str, str]]:
    ids = get_all_ids()
    values = []
    for id in ids:
        count = len(get_values_by_time_and_id(start_date, id))
        values.append((id, str(count)))
    return values


def add_to_db(user_id: str, time: str, browser: str):
    items = list(get_all_values())
    with open(DATABASE_FILE_PATH, 'w+') as f:
        items.append((user_id, time, browser))
        data = ''
        for item in items:
            data += item[0] + ': ' + item[1] + ': ' + item[2] + '\n'
        f.write(data)


def clean_db():
    with open(DATABASE_FILE_PATH, 'w+') as f:
        f.write('')

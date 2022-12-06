from datetime import datetime, timedelta


def get_all_values() -> list[tuple[str, str]]:
    with open('db.txt', 'r') as f:
        lines = f.readlines()
        
        if len(lines) == 0: return []

        items = []
        for line in lines:
            a, b = line.split(': ')[0], line.split(': ')[1][:-1]
            items.append((a, b))
        return items


def get_values_by_time(start_date: datetime) -> list[tuple[str, str]]:
    values = get_all_values()
    if start_date + timedelta(days=0.5) > datetime.utcnow():
        return list(values)
    return [value for value in values if datetime.utcfromtimestamp(value[1]) > start_date]


def get_values_by_time_and_id(start_date: datetime, id: str) -> list[tuple[str, str]]:
    values = get_values_by_time(start_date)
    return [value for value in values if value[0] == id]


def get_all_ids() -> list[str]:
    values = get_all_values
    return list(set([value[0] for value in values]))


def get_values_count_visits_by_time(start_date: datetime) -> list[tuple[str, str]]:
    ids = get_all_ids()
    values = []
    for id in ids:
        count = len(get_values_by_time_and_id(start_date, id))
        values.append((id, str(count)))
    return values


def add_to_db(user_id: str, time: str):
    items = list(get_all_values())
    with open('db.txt', 'w+') as f:
        items.append((user_id, time))
        data = ''
        for item in items:
            print(item)
            data += item[0] + ': ' + item[1] + '\n'
        f.write(data)

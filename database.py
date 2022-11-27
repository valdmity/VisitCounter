def get_values_frob_db() -> dict[str, list[str]]:
    with open('db.txt', 'r') as f:
        data = f.readline()[1:-1].split(', ')
        
        if len(data) == 0: return dict()

        return dict([(line.split(': ')[0][1:-1], line.split(': ')[1][1:-1]) for line in data])


def add_to_db(user_id: str, time: str):
    items = get_values_frob_db()
    with open('db.txt', 'w+') as f:
        if user_id not in items:
            items[user_id] = []
        items[user_id].append(time)
        f.write(str(items))

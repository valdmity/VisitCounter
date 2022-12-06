def get_values_frob_db() -> list[tuple[str, str]]:
    with open('db.txt', 'r') as f:
        lines = f.readlines()
        
        if len(lines) == 0: return []

        items = []
        for line in lines:
            a, b = line.split(': ')[0], line.split(': ')[1][:-1]
            items.append((a, b))
        return items



def add_to_db(user_id: str, time: str):
    items = list(get_values_frob_db())
    with open('db.txt', 'w+') as f:
        items.append((user_id, time))
        data = ''
        for item in items:
            print(item)
            data += item[0] + ': ' + item[1] + '\n'
        f.write(data)

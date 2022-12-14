from objects.Table import Table, Row


def parse_arr(array: list):
    array.pop()
    for i in range(len(array)):
        array[i] = array[i].strip()
    return array


def load_table(filename):
    if not filename.endswith('.txt'):
        raise TypeError('Cannot load')
    result = Table()
    with open(filename, 'r+') as file:
        headers = parse_arr(file.readline().split('|'))
        for j in file:
            arr = parse_arr(j.split('|'))
            r = {headers[i]: arr[i] for i in range(len(arr))}
            result.rows.append(Row(r))
    return result


def save_table(table, filename):
    if not isinstance(table, Table):
        raise TypeError
    if table.is_empty():
        with open(filename, 'w') as f:
            return
    with open(filename, 'w+') as file:
        template = "{:{align}{width}}|"
        for k in table.rows[0].keys():
            file.write(template.format(k, align='^', width='15'))
        for j in table.rows:
            file.write('\n')
            for i in j.keys():
                file.write(template.format(j[i], align='^', width='15'))

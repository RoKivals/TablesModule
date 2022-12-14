from objects.Table import Table, Row


def get_key_by_number(dict_keys, number):
    d = 0
    for k in dict_keys:
        if d == number:
            return k
        d += 1
    return None


def get_rows_by_number(table: Table, start: int, stop: int = None, copy_table=False):
    if not isinstance(table, Table) or not isinstance(copy_table, bool):
        raise TypeError
    if start < 0 or stop >= len(table.rows):
        raise ValueError

    if copy_table:
        new_table = Table(*table.rows)
    else:
        new_table = table

    if stop is None:
        new_table.rows = table.rows[start]
    else:
        new_table.rows = table.rows[start:stop]
    return new_table


def get_rows_by_index(table: Table, *values, copy_table=False):
    if not isinstance(table, Table) or not isinstance(copy_table, bool):
        raise TypeError

    if copy_table:
        new_table = Table(*table.rows)
    else:
        new_table = table

    del_indexes = []
    fir_key = get_key_by_number(table.rows[0].keys(), 0)
    for x in table.rows:
        if x.get(fir_key) not in values:
            del_indexes.append(x)
    for i in del_indexes:
        new_table.rows.remove(i)
    return new_table


def print_table(table: Table):
    if not isinstance(table, Table):
        raise TypeError
    print(table)


a = Table(
    Row(dict(name='Slava', surname='Elan')),
    Row(dict(name="Sosat", surname="Blta")),
    Row(dict(name="Sany", surname="Bsu")))

get_rows_by_index(a, 'Slava', 'Sany', copy_table=True)
print(a)

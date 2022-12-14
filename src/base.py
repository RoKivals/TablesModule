from objects.Table import Table, Row
import re


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
    new_table = Table()
    fir_key = list(table.rows[0].keys())[0]
    for x in table.rows:
        if x.get(fir_key) in values:
            new_table.rows.append(x)
    if not copy_table:
        table.rows = new_table.rows
    return new_table


def get_column_types(table: Table, by_number=True):
    if not isinstance(table, Table) or not isinstance(by_number, bool):
        raise TypeError
    ans = dict()
    if table.is_empty():
        return ans

    cols = list(table.rows[0].keys())
    for number, name in enumerate(cols):
        dtype = str(type(table.rows[0].get(name)))
        dtype = ''.join(re.findall(r"'([^']+)'", dtype))
        if by_number:
            ans[number] = dtype
        else:
            ans[name] = dtype
    return ans


# ЧТО БЛЯТЬ!?
def set_column_types(table: Table, ):
    pass


def print_table(table: Table):
    if not isinstance(table, Table):
        raise TypeError
    print(table)


a = Table(
    Row(dict(name='Slava', surname='Elan')),
    Row(dict(name="Sosat", surname="Blta")),
    Row(dict(name="Sany", surname="Bsu")))

get_rows_by_index(a, 'Slava', 'Sany', copy_table=False)
l = get_column_types(a)
print(l)

from objects.Table import Table, Row
import re
from copy import deepcopy
from pydoc import locate


def get_rows_by_number(table: Table, start: int, stop: int = None, copy_table=False):
    if not isinstance(table, Table) or not isinstance(copy_table, bool):
        raise TypeError
    if start < 0 or stop >= len(table.rows):
        raise ValueError

    if copy_table:
        new_table = deepcopy(table)
    else:
        new_table = Table(table.rows)

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
            if not copy_table:
                x = deepcopy(x)
            new_table.rows.append(x)
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


def set_column_types(table: Table, types_dict: dict, by_number=True):
    if not isinstance(table, Table) or not isinstance(by_number, bool):
        raise TypeError
    if table.is_empty():
        return table

    # Ключи словаря с типами
    types_keys = list(types_dict.keys())

    # Список ключей исходной таблицы
    cols = list(table.rows[0].keys())
    for i in types_keys:
        # Объект позволяет менять тип по названию типа
        changer = locate(types_dict[i])
        for j in table.rows:
            if by_number:
                j[cols[i]] = changer(j[cols[i]])
            else:
                j[i] = changer(j[i])


def get_values(table: Table, column=0):
    if not isinstance(table, Table) or not isinstance(column, int | str):
        raise TypeError
    ans = []
    if isinstance(column, int):
        pass
    return ans


'''
get_values(column=0) – получение списĸа значений
(типизированных согласно типу столбца) таблицы из столбца либо
по номеру столбца (целое число, значение по умолчанию 0, либо
по имени столбца).
'''


def print_table(table: Table):
    if not isinstance(table, Table):
        raise TypeError
    print(table)


a = Table(
    Row(dict(name="Slava", surname='Elan')),
    Row(dict(name="Sosat", surname="Blta")),
    Row(dict(name="Sany", surname="Bsu")))

print(a)
print('\n\n')

b = get_rows_by_index(a, 'Slava', 'Sany', copy_table=True)
set_column_types(a, types_dict={0: 'str', 1: 'bool'})
print(a)

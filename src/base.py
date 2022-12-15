from objects.Table import Table, Row
import re
from copy import deepcopy
from pydoc import locate


def get_rows_by_number(table: Table, start: int, stop: int = None, copy_table=False):
    if not isinstance(table, Table) or not isinstance(copy_table, bool):
        raise TypeError
    if start < 0 or stop >= len(table.rows):
        raise RuntimeError

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
            if copy_table:
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
    if table.is_empty():
        return ans

    cols = list(table.rows[0].keys())
    if isinstance(column, int):
        if column < 0 or column >= len(cols):
            raise RuntimeError("Not found column")
    if isinstance(column, str):
        if column not in cols:
            raise RuntimeError("Not found column")

    for j in table.rows:
        if isinstance(column, int):
            ans.append(j[cols[column]])
        elif isinstance(column, str):
            ans.append(j[column])
    return ans


def get_value(table: Table, column=0):
    ans = get_values(table, column)[0]
    return ans


def set_values(table: Table, values, column=0):
    if not isinstance(table, Table) or not isinstance(column, int | str):
        raise TypeError
    if table.is_empty():
        raise RuntimeError("Table is empty")

    cols = list(table.rows[0].keys())
    if isinstance(column, int):
        if column < 0 or column >= len(cols):
            raise RuntimeError("Not found column")
    if isinstance(column, str):
        if column not in cols:
            raise RuntimeError("Not found column")

    for i, j in zip(table.rows, values):
        if isinstance(column, int):
            i[cols[column]] = j
        elif isinstance(column, str):
            i[column] = j


def set_value(table: Table, value, column=0):
    set_values(table, [value], column)


def print_table(table: Table):
    if not isinstance(table, Table):
        raise TypeError
    print(table)

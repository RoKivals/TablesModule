import csv

from objects.Table import Table, Row


def load_table(filename):
    if not filename.endswith('.csv'):
        raise TypeError('Cannot load')
    result = Table()
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i in reader:
            row = Row(i)
            result.rows.append(row)
    return result


def save_table(table, filename):
    if not isinstance(table, Table):
        raise TypeError
    if table.is_empty():
        with open(filename) as _:
            return
    fieldnames = list(table.rows[0].keys())
    with open(filename, 'w+', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in table.rows:
            writer.writerow(row)

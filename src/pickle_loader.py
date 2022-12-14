import pickle

from objects.Table import Table


def load_table(filename):
    if not filename.endswith('.pickle'):
        raise TypeError('Cannot load')
    with open(filename, 'rb') as file:
        result = pickle.load(file)
    return result


def save_table(table, filename):
    if not isinstance(table, Table):
        raise TypeError
    if table.is_empty():
        with open(filename, 'wb') as _:
            return
    with open(filename, 'wb') as pickle_file:
        pickle.dump(table, pickle_file)

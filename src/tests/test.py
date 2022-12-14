import unittest
from objects.Table import Table
from objects.Row import Row
import csv_loader as cs


# def test2():
#     a = Table(
#         Row(dict(name='Slava', surname='Elan')),
#         Row(dict(name="Sosat", surname="Blta")))
#
#     save_table(a, "a.pickle")
#
#     b = load_table("a.pickle")
#     for row in b.rows:
#         print(row)

# a = Table(
#     Row(dict(name='Slava', surname='Elan')),
#     Row(dict(name="Sosat", surname="Blta")))
# save_table(a, "bla.txt")
# b = load_table("bla.txt")


class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Table(
            Row(dict(name='Slava', surname='Elan')),
            Row(dict(name="Sosat", surname="Blta")))
        cs.save_table(a, "bla.csv")
        b = cs.load_table("bla.csv")
        self.assertEqual(a.rows, b.rows)  # add assertion here


if __name__ == '__main__':
    unittest.main()

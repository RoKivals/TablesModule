import unittest
from objects.Table import Table
from objects.Row import Row
import csv_loader as cs
import pickle_loader as pck
import txt


class MyTestCase(unittest.TestCase):
    def testcsv(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        cs.save_table(a, "first.csv")
        b = cs.load_table("first.csv")
        self.assertEqual(a.rows, b.rows)
        # add assertion here

    def testpickle(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        pck.save_table(a, "file.pickle")
        b = pck.load_table("first.pickle")
        self.assertEqual(a.rows, b.rows)

    def testtxt(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        txt.save_table(a, "first.txt")
        b = txt.load_table("first.txt")
        c = Table()
        txt.save_table(c, 'empty.txt')
        f = txt.load_table('empty.txt')
        self.assertEqual(a.rows, b.rows)
        self.assertEqual(c.rows, f.rows)


if __name__ == '__main__':
    unittest.main()

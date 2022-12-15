import unittest

import txt
from objects.Table import Table, Row
import csv_loader as cs
import pickle_loader as pck


class MyTestCase(unittest.TestCase):
    def testcsv(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        cs.save_table(a, "src/tests/first.csv")
        b = cs.load_table("src/tests/first.csv")
        self.assertEqual(a.rows, b.rows)
        # add assertion here

    def testpickle(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        pck.save_table(a, "src/tests/file.pickle")
        b = pck.load_table("src/tests/file.pickle")
        self.assertEqual(a.rows, b.rows)

    def testtxt(self):
        a = Table(
            Row(dict(name='Slava', surname='Orus', town='MSC')),
            Row(dict(name="Veronika", surname="Boiko", town='Tver')),
        )
        txt.save_table(a, "src/tests/first.txt")
        print(a)
        b = txt.load_table("src/tests/first.txt")
        c = Table()
        txt.save_table(c, 'src/tests/empty.txt')
        f = txt.load_table('src/tests/empty.txt')
        self.assertEqual(a.rows, b.rows)
        self.assertEqual(c.rows, f.rows)


if __name__ == '__main__':
    unittest.main()

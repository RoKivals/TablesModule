from objects.Row import Row


class Table:
    def __init__(self, *args: Row):
        self._rows = list(args)

    def __str__(self):
        ans = ''
        if len(self._rows) == 0:
            return ans
        template = "{:{align}{width}}|"
        for k in self._rows[0].keys():
            ans += template.format(k, align='^', width='15')
        for j in self._rows:
            ans += '\n'
            for i in j.keys():
                ans += template.format(j[i], align='^', width='15')
        return ans

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, array: list):
        self._rows = array

    def is_empty(self):
        return not len(self.rows)

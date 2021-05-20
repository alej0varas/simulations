class FormationSimplest:
    def __init__(self):
        self._units = []
        self._formation = None

    def add_units(self, units):
        if not isinstance(units, list):
            units = [units]
        c = 0
        for u in units:
            if u not in self._units:
                self._units.append(u)
                c += 1
        return c

    def form_units(self):
        if not self._units:
            return
        self._formation = [[], [],[]]
        for i in range(len(self._units)):
            self._formation[i % 3].append(self._units[i])
        if len(self._units) > 3 * 2 + 1:
            fst_squad_len = len(self._formation[0]) - 1
            try:
                self._formation[2][fst_squad_len]
            except IndexError:
                self._formation[2].append(self._formation[1].pop())
                tmp = self._formation[1].pop()
                self._formation[1].append(None)
                self._formation[1].append(tmp)

class FormationSimplest:
    def __init__(self):
        self._units = []
        self._units_positions = {}

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
        for i in range(len(self._units)):
            self._units_positions[(i % 3, i // 3)] = self._units[i]

        if len(self._units) > 3 * 2 + 1:
            i = (len(self._units) - 1) // 3
            last_tail = (2, i)
            second_last = 2 - 1
            try:
                self._units_positions[last_tail]
                return
            except KeyError:
                j = i
                while True:
                    try:
                        self._units_positions[last_tail] = self._units_positions[(second_last, j)]
                        self._units_positions[(second_last, j)] = None
                        break
                    except KeyError:
                        j -= 1
                for k in range(1, 2):
                    j = i - 1
                    while True:
                        try:
                            self._units_positions[(k, i)] = self._units_positions[(k, j)]
                            self._units_positions[(k, j)] = None
                            break
                        except KeyError:
                            j -= 1

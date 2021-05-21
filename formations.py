class FormationSimplest:
    def __init__(self, number_of_lines=3):
        self._units = []
        self._units_positions = {}
        self.number_of_lines = number_of_lines

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
            self._units_positions[(i % self.number_of_lines, i // self.number_of_lines)] = self._units[i]

        if len(self._units) > self.number_of_lines * 2 + 1 and len(self._units) % self.number_of_lines > 1:
            # If true means there's enough units to close the tail of the formation. Closing the tail is:
            # Going from > to
            # u u u     u u u
            # u u u  >  u   u
            #   u u     u u u
            second_last = self.number_of_lines - 2
            line_length = len(self._units) // self.number_of_lines
            for i in range(second_last, 0, -1):
                if self._units_positions.get((i + 1, line_length)) is None:
                    self._units_positions[(i + 1, line_length)] = self._units_positions[(i, line_length - 1)]
                    self._units_positions[(i, line_length - 1)] = None

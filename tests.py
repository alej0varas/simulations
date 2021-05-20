import math
import unittest

import formations
import simulation
import units


class TestUnitSimplestClass(unittest.TestCase):
    def test_has_position(self):
        self.assertEqual(units.UnitSimplest().position, 0)

    def test_has_speed(self):
        self.assertEqual(units.UnitSimplest().speed, 0)

    def test_has_acceleration(self):
        self.assertEqual(units.UnitSimplest().get_acceleration(), 0)

    def test_can_accelerate(self):
        u = units.UnitSimplest()

        u.tick()

        self.assertEqual(u.position, 0)
        self.assertEqual(u.speed, 0)

        u.set_direction(1)
        u.tick()

        self.assertEqual(u.speed, 1 / simulation.TICKS_PER_SECOND)
        self.assertEqual(u.position, 1 / simulation.TICKS_PER_SECOND)

        u.tick()

        self.assertEqual(u.speed, 2 / simulation.TICKS_PER_SECOND)
        self.assertEqual(u.position, 3 / simulation.TICKS_PER_SECOND)

        u.tick()

        self.assertEqual(u.speed, 2 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 5 / simulation.TICKS_PER_SECOND))

        u.set_direction(-1)
        u.tick()

        self.assertTrue(math.isclose(u.speed, 1 / simulation.TICKS_PER_SECOND))
        self.assertTrue(math.isclose(u.position, 6 / simulation.TICKS_PER_SECOND))

        u.tick()

        self.assertEqual(u.speed, 0 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 6 / simulation.TICKS_PER_SECOND))

        u.tick()

        self.assertEqual(u.speed, -1 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 5 / simulation.TICKS_PER_SECOND))

        u.tick()

        self.assertEqual(u.speed, -1 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 4 / simulation.TICKS_PER_SECOND))

        u.set_direction(0)
        u.tick()

        self.assertEqual(u.speed, -1 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 3 / simulation.TICKS_PER_SECOND))

        u.tick()

        self.assertEqual(u.speed, -1 / simulation.TICKS_PER_SECOND)
        self.assertTrue(math.isclose(u.position, 2 / simulation.TICKS_PER_SECOND))

    def test_has_name(self):
        # TODO: use a global counter for unnamed clases
        u = units.UnitSimplest()

        self.assertEqual(str(u), '(unnamed)')

        u = units.UnitSimplest('rose')

        self.assertEqual(str(u), 'rose')

        self.assertEqual(repr(u), 'units.UnitSimplest(rose)')

        u = units.UnitSimplest(0)

        self.assertEqual(str(u), '0')


class FormationSimplestTentCase(unittest.TestCase):
    def test_can_add_unit(self):
        f = formations.FormationSimplest()
        u = units.UnitSimplest()

        f.add_units(u)

        self.assertEqual(f._units, [u])

        r = f.add_units(u)

        self.assertEqual(r, 0)

        u1 = units.UnitSimplest()
        r = f.add_units(u1)

        self.assertEqual(f._units, [u, u1])

        u2 = units.UnitSimplest()
        r = f.add_units([u2])

        self.assertEqual(f._units, [u, u1, u2])

    def test_can_form_units(self):
        f = formations.FormationSimplest()

        f.form_units()

        self.assertEqual(f._formation, None)

        u = units.UnitSimplest(0)
        f.add_units(u)

        f.form_units()

        self.assertEqual(f._formation, [[u], [], []])

        u1 = units.UnitSimplest(1)
        f.add_units(u1)

        f.form_units()

        self.assertEqual(f._formation, [[u], [u1], []])

        u2 = units.UnitSimplest(2)
        f.add_units(u2)

        f.form_units()

        self.assertEqual(f._formation, [[u], [u1], [u2]])

        u3 = units.UnitSimplest(3)
        f.add_units(u3)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3], [u1], [u2]])

        u4 = units.UnitSimplest(4)
        f.add_units(u4)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3], [u1, u4], [u2]])

        u5 = units.UnitSimplest(5)
        f.add_units(u5)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3], [u1, u4], [u2, u5]])

        u6 = units.UnitSimplest(6)
        f.add_units(u6)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3, u6], [u1, u4], [u2, u5]])

        u7 = units.UnitSimplest(7)
        f.add_units(u7)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3, u6], [u1, None, u4], [u2, u5, u7]])

        u8 = units.UnitSimplest(8)
        f.add_units(u8)

        f.form_units()

        self.assertEqual(f._formation, [[u, u3, u6], [u1, u4, u7], [u2, u5, u8]])



if __name__ == "__main__":
    unittest.main()

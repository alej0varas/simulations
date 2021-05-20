#!/usr/bin/env python

# Entry point for whatever this becomes.

import time

import simulation
import unit


def main():
    simulation.main()
    print('ready')
    while True:
        simulation.add(unit.UnitSimplest())
        time.sleep(.001)


if __name__ == "__main__":
    main()

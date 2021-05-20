import threading
import time

TICKS_PER_SECOND = 30
NANO_SECONDS = 10 ** 9
NANO_SECONDS_PER_TICK = NANO_SECONDS / TICKS_PER_SECOND

_objects = []


def add(obj):
    _objects.append(obj)


def run(objects):
    ups = 0
    skiped = 0
    last_second = time.time()
    while True:

        start = time.time_ns()
        end = start + NANO_SECONDS_PER_TICK

        for obj in objects:
            obj.tick()

        if int(time.time()) > last_second:
            print('UPS:', ups)
            print('SKIPED:', skiped)
            print('OBJ #:', len(objects))
            ups = 0
            skiped = 0
            last_second = time.time()

        sleep_ns = (end - time.time_ns()) / NANO_SECONDS

        if sleep_ns >= 0:
            time.sleep(sleep_ns)
            ups += 1
        else:
            skiped += 1


def main():
    t = threading.Thread(target=run, args=(_objects, ))
    t.start()

import simulation


class UnitSimplest:
    """Something that exists and act in the world. Moves in only one
    axe. Accelerate `acceleration` units per second."""

    def __init__(self, name='(unnamed)', acceleration=1, direction=0, speed=0, position=0, max_speed=2, max_backward_speed=-1):
        self.acceleration = acceleration / simulation.TICKS_PER_SECOND
        self.direction = direction
        self.speed = speed
        self.position = position
        self.max_speed = max_speed / simulation.TICKS_PER_SECOND
        self.max_backward_speed = max_backward_speed / simulation.TICKS_PER_SECOND
        if isinstance(name, int):
            name = str(name)
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__class__.__module__ + '.' + type(self).__name__ + '(' + str(self) + ')'

    def get_acceleration(self):
        acceleration = self.acceleration * self.direction
        if self.max_backward_speed <= self.speed + acceleration <= self.max_speed:
            return acceleration
        return 0

    def set_direction(self, direction):
        self.direction = direction

    def tick(self):
        self.speed += self.get_acceleration()
        self.position += self.speed

class airplane:
    def __init__(self, spawn_location, health, initial_velocity = [0,0,0],
                 initial_acceleration = [0,0,0]):
        self.spawn_location = spawn_location
        self.location = spawn_location
        self.health = health
        self.velocity = initial_velocity
        self.acceleration = initial_acceleration

    def set_acceleration(self, ax, ay, az):
        self.acceleration = [ax, ay, az]

    def calculate_next_velocity(self, time):
        for i in range(3):
            self.velocity[i] += self.acceleration[i]*time

    def calculate_next_location(self, time):
        for i in range(3):
            self.location[i] += (self.velocity[i]*time +
                                 0.5*self.acceleration[i]*time**2)
    

class airplane:
    '''airplane class: 
    Attributes: location, health, velocity, acceleration
    Functions: set acceleration, velocity and location. 
    AirPlane object is controlled by set acceleration function'''
    def __init__(self, spawn_location:[float,float,float], health, initial_velocity:[float,float,float],
        initial_acceleration :[float,float,float]):
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
  

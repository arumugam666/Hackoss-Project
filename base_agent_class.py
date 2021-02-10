from abc import ABC, abstractmethod

class base_agent_class(ABC):

    ''' base agent class: 
    information given: velocity, location, acceleration, target and trap locations.
    what agents can do: change directions, shoot others(not implemented yet)'''

    def __init__(self, *args):
        print(args)

    @abstractmethod
    def step(self,state):
        ''' Passing info and change directions'''
        pass

    def calculate_target_distance(self,self_location,target_location):
        ''' help function: calculate distance to all the targets'''
        target_distance = []
        for i in range (0,len(target_distance)):
            distance = (self_location[0] - target_location[i][0])**2 + (self_location[1] - target_location[i][1])**2 + (self_location[2] - target_location[i][2])**2
            distance = sqrt(distance)
            target_distance.append(distance)

        return target_distance

    def calculate_trap_distance(self,self_location,trap_distance):
        ''' help function: calculate distance to all the traps'''
        trap_distance = []
        for i in range (0,len(trap_distance)):
            distance = (self_location[0] - trap_location[i][0])**2 + (self_location[1] - trap_location[i][1])**2 + (self_location[2] - trap_location[i][2])**2
            distance = sqrt(distance)
            trap_distance.append(distance)

        return trap_distance


        

        
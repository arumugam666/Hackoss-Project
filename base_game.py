from abc import ABC, abstractmethod
''' Class definition for base game '''

class base_game(ABC):
    def __init__(self, num_targets, num_airplanes):
        self.num_airplanes = num_airplanes
        self.num_targets = num_targets
        self.target_history = []
        for i in range(num_airplanes):
            self.target_history.append([])

    @abstractmethod
    def game_step(self, airplanes, targets, trap):
        return

    @abstractmethod
    def write_to_history():
        return

    @abstractmethod
    def display_game():
        return

    '''Function checks if an airplane has reached a target within a certain tolerance and stores the information
    in target history '''
    def change_target_history(self, airplanes, targets, tolerance):
        for i in airplanes:
            for j in targets:
                if(same_location(i.location, j.location, tolerance) and j not in target_hist[airplanes.index(i)]):
                    target_hist[airplanes.index(i)].append(j)
                    

    '''Function to check if two locations are the same within a certain tolerance '''
    def check_same_location(locationA, locationB, tolerance):
        same_location = True
        for i in range(3):
            if (locationA[i] - locationB[i]) > tolerance or (locationA[i] - locationB[i]) < tolerance:
                same_location = False
        return same_location

    ''' Function checks if any airplane has gone through all the targets. The function returns the index of the airplane that
        has won the game. It returns negative one if no airplanes have won the game yet '''
    def check_win(target_hist):
        for i in target_hist:
            if len(i) >= num_targets:
                return target_hist.index(i)
        return -1
                
        


        
    





    




    

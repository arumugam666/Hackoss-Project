from datetime import datetime


class Map:
    """
    Map Class
    Attributes: Number of targets (tracks number of targets),
                List of Airplanes (tracks airplanes in the map),
                List of Traps (tracks traps in the map)
    Methods: lap
    """
    def __init__(self, targets: int, airplane=[], traps=[]):
        self.targets = targets
        self.airplane = airplane
        self.traps = traps
        self.time = datetime.now
        self.leaderboard = []

    def lap(self):
        """
        Calculates the time taken for each airplane to go through all hoops. Called if any airplane passed all targets
        :return: updates the leaderboard attribute with a tuple (minutes, seconds) based on the time taken
        """
        curr = datetime.now  # get the current time
        diff = (self.time - curr).total_seconds()
        minutes = diff / 60  # get minutes passed
        seconds = round(diff - (minutes * 60))
        self.leaderboard.append((minutes, seconds))

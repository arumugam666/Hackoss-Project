from datetime import datetime

class Map:
    def __init__(self, targets, airplane=[]):
        self.targets = targets
        self.airplane = airplane
        self.time = datetime.now
        self.leaderboard = []

    def lap(self):
        curr = datetime.now  # get the current time
        diff = (self.time - curr).total_seconds()
        minutes = diff / 60  # get minutes passed
        seconds = round(diff - (minutes * 60))
        self.leaderboard.append((minutes, seconds))

    def checkTargets(self):
        #check if location of plane == location of targets. if so then add points for airplane

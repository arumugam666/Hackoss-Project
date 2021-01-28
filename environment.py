import numpy as np
import random


class TicTacToeEnv:

    def __init__(self, agents=[]):
        super().__init__()

        self.board = [[0 for x in range(3)] for y in range(3)]
        self.turn = 1
        self.agents = agents

    def getPossibleMoves(self):
        possible_moves = []
        for indx, row in enumerate(self.board):
            for indy, element in enumerate(row):
                if element == 0:
                    possible_moves.append((indx, indy))

        return possible_moves

    def gameStep(self):

        for agent in self.agents:
            action = random.choice(self.getPossibleMoves())
            # action = agent.step(self.board)
            self.agentStep(self.turn, action)
            print(self)
            if self.checkWin(self.turn):
                return True
            self.turn *= -1

    def agentStep(self, agentId, action):
        self.board[action[0]][action[1]] = agentId

    def __repr__(self):
        representation = str(np.array(self.board))
        representation.replace("-1", "O")
        representation.replace("1", "X")
        representation.replace("0", "_")
        return representation

    def checkWin(self, agentId):
        for row in self.board:
            if agentId*sum(row) == 3:
                return True

        for indy in range(3):
            accum = 0
            for indx in range(3):
                accum += self.board[indx][indy]

            if agentId*accum == 3:
                return True

        if agentId*(self.board[0][0] + self.board[1][1] + self.board[2][2]) == 3:
            return True
        if agentId*(self.board[2][0] + self.board[1][1] + self.board[0][2]) == 3:
            return True


if __name__ == "__main__":
    env = TicTacToeEnv(agents=[1, 1])
    while not env.gameStep():
        pass
        # class Agent:

        #     def Agent

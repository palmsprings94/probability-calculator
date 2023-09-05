import random
import copy

class Hat:

    def __init__(self, **hats):
        self.hats = hats
        self.contents = []
        for i in self.hats:
            for _ in range(self.hats[i]):
                self.contents.append(i)

    def draw(self, x):
        drawnballs = []
        if x > len(self.contents):
            x = 0
        while x > 0:
            random_ball = random.choice(self.contents)
            self.contents.remove(random_ball)
            drawnballs.append(random_ball)
            x = x - 1
        return drawnballs


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ehat = []
    m = 0
    for i in expected_balls:
        for _ in range(expected_balls[i]):
            ehat.append(i)
    for _ in range(num_experiments):
        nhat = copy.deepcopy(hat)
        bawlsdrawn = nhat.draw(num_balls_drawn)
        if any(item in bawlsdrawn for item in ehat):
            m = m + 1
    probability = m / num_experiments
    
    return probability

import requests
import math

class Wire:
    def __init__(self, data: list):
        self.data: list = data
        self.position: tuple = (0, 0)
        self.path: list = []

    jump = {
        "U": lambda x, y : (x, y + 1),
        "D": lambda x, y : (x, y - 1),
        "L": lambda x, y : (x + 1, y),
        "R": lambda x, y : (x - 1, y)
    }

    def trace(self):
        for action in self.data:
            step = int(action[1:])
            direction = action[0]

            while step > 0:
                x, y = self.position
                self.position = self.jump[direction](x, y)
                self.path.append(self.position)
                step -= 1



if __name__== "__main__":

    response = requests.get("https://adventofcode.com/2019/day/3/input", headers={"Cookie":"session=53616c7465645f5f5966fe32801f52f3ccdcfda4336dfce8c64ce2f469c48c2688e46a073403cda4de928b6ae1a21e2d"})

    if response.status_code == 200:
        input = response.text.splitlines()

        trace = {}

        wire1 = Wire(input[0].split(","))
        wire2 = Wire(input[1].split(","))

        wire1.trace()
        print("wire 1 traced")
        wire2.trace()
        print("wire 2 traced")

        trace1 = set(wire1.path)
        trace2 = set(wire2.path)
        intersections = list(trace1 & trace2)
     
        if(intersections):
            closestPoint = math.inf

            for (x, y) in intersections:
                manhattanDistance = abs(x) + abs(y)
                closestPoint = min(closestPoint, manhattanDistance)
              
            print("the closest intersection is {0} steps away".format(closestPoint))


    else :
        print("Could not retrieve data")
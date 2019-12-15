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


        # wire1 = Wire("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(','))
        # wire2 = Wire("U62,R66,U55,R34,D71,R55,D58,R83".split(','))
        
        wire1 = Wire(input[0].split(","))
        wire2 = Wire(input[1].split(","))

        wire1.trace()
        wire2.trace()
     
        trace1 = set(wire1.path)
        trace2 = set(wire2.path)

        intersections = list(trace1 & trace2)
     
        if(intersections):
            closestPoint = math.inf

            for (x, y) in intersections:
                # manhattanDistance = abs(x) + abs(y)
                # closestPoint = min(closestPoint, manhattanDistance)
                stepsWire1 = wire1.path.index((x, y)) + 1
                stepsWire2 = wire2.path.index((x, y)) + 1 
                totalSteps = stepsWire1 + stepsWire2

                closestPoint = min(closestPoint, totalSteps)

                
                
            print("the shortest intersection takes {0} steps.".format(closestPoint))


    else :
        print("Could not retrieve data")
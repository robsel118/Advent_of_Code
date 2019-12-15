from functools import reduce
import math
import os
import requests

def calculateFuel(acc: int, mass: str):
    fuel: int = getFuelPerMass(mass)
    moduleFuel: int = 0
    while fuel > 0:
        moduleFuel += fuel
        fuel = getFuelPerMass(fuel)

    return acc + moduleFuel


def getFuelPerMass(mass: str): 
    return math.floor(int(mass)/3) - 2 


if __name__== "__main__":
    response = requests.get("https://adventofcode.com/2019/day/1/input", headers={"Cookie":"session=53616c7465645f5f5966fe32801f52f3ccdcfda4336dfce8c64ce2f469c48c2688e46a073403cda4de928b6ae1a21e2d"})
    if response.status_code == 200:
        input = response.text.splitlines()
        total_fuel = reduce(calculateFuel, input,0)
        print(total_fuel)
    else :
        print("Could not tertieve data")


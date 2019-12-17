
import requests


def addition(data: list, sequence: list):
    x, y, output = extract_adress(sequence)
    data[output] = data[x] + data[y]

def multiply(data, sequence):
    x, y, output = extract_adress(sequence)
    data[output] = data[x] * data[y]

def extract_adress(sequence):
    xIndex:int = sequence[0]
    yIndex:int = sequence[1]
    outputIndex: int = sequence[2]

    return xIndex,yIndex,outputIndex

def run (input, noun, verb):
    input[1] = noun
    input[2] = verb

    for i in range(0, len(input) - 1, 4):

        opcode = input[i]
        
        if opcode == 99:
            break
        elif opcode == 1:
            addition(input, input[i+1:i+4])
        elif opcode == 2:
            multiply(input, input[i+1:i+4])

    return input[0]

if __name__== "__main__":

    response = requests.get("https://adventofcode.com/2019/day/2/input", headers={"Cookie":"session=53616c7465645f5f5966fe32801f52f3ccdcfda4336dfce8c64ce2f469c48c2688e46a073403cda4de928b6ae1a21e2d"})
    
    if response.status_code == 200:
        input = response.text.split(",")
        # convert to int
        input = [int(i) for i in input]
        exit = False
        
        for noun in range(0, 99):
            for verb in range(0, 99):
                output = run(input.copy(), noun, verb)
                exit = output == 19690720
                if exit:
                    print("the output 19690720 at position 0 require the noun {0} and the verb {1}".format(noun, verb))
                    break
            if exit:
                break
    else :
        print("Could not retrieve data")
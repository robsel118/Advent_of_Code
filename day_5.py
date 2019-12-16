
import requests

USER_INPUT = 1

def addition(data: list, x:int , y: int, output:int):
    # print("address {0} was set the value of {1} + {2}".format(output, x, y))
    data[output] = x + y

def multiplication(data: list, x:int , y: int, output:int):
    # print("address {0} was set the value of {1} * {2}".format(output, x, y))
    data[output] = x * y

def store(data:list, adress:int):
    # print("address {0} was set the value of 1".format(adress))

    data[adress] = USER_INPUT

def output(data:list, output: int ):
    
    print(data[output])
    # print("------------------------\n")

operations = {
    "1" : {
        "action": addition,
        "param": 3
    },
    "2" : {
        "action": multiplication,
        "param": 3
    },
    "3" : {
        "action": store,
        "param": 1
    },
    "4" : {
        "action": output,
        "param": 1
    },
}

def process(data:list, instruction:str, params: list):
    args = [0, 0]
    modes = []
    opcode = instruction[-1:]
    if len(instruction) != 1 and opcode != "3":
        modes= (instruction.zfill(4))[:-2]
  
        modes = modes[::-1]
        # print ("Instruction {0} with params {1} and modes {2} at {3}".format(instruction, args,modes,  params))   
        for index, param in enumerate(params[:-1]):
           
            if modes[index] == "0":
                args[index] = data[param]
            elif modes[index] == "1":
                args[index] = param
    else: 
        args[0] = params[0]
      
        if opcode == "4" or opcode == "3":
            args[0] = params[0]
        else:
            args[0] = data[params[0]]
            args[1] = data[params[1]]

    operate(data, opcode, args,params)

def operate(data: list, opcode:str, args:list, params:list):
    if (opcode == "1" or opcode == "2"):
        operations[opcode]["action"](data, args[0], args[1], params[2])
    elif opcode == "3" or opcode == "4":
        operations[opcode]["action"](data, args[0])    
 
    

def run (data: list):
    position = 0
    while position < len(data):
        instruction = str(data[position])
        if instruction == "99": 
            break
        
        opcode = instruction[-1:]
        nbOfParams = operations[opcode]["param"]
        params = data[position + 1 : position + nbOfParams + 1] 
       
        process(data, instruction, params)
        nextPosition = position + nbOfParams + 1
        position = nextPosition

if __name__== "__main__":

    response = requests.get("https://adventofcode.com/2019/day/5/input", headers={"Cookie":"session=53616c7465645f5f5966fe32801f52f3ccdcfda4336dfce8c64ce2f469c48c2688e46a073403cda4de928b6ae1a21e2d"})

    if response.status_code == 200:
        data = response.text.split(",")
        # convert to int
        data = [int(i) for i in data]
        # data = [1001,1,2,4,33, 0]
        run (data)
        print(data)
    else :
        print("Could not retrieve data")
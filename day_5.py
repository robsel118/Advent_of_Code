
import requests




class Computer:
    def __init__(self, memory, statusCode):
        self.cursor = 0
        self.memory = memory
        self.statusCode= statusCode

    def addition(self, x:int , y: int,  output:int):
        # print("address {0} was set the value of {1} + {2}".format(output, x, y))
        self.memory[output] = x + y

    def multiplication(self, x:int , y: int, output:int):
        # print("address {0} was set the value of {1} * {2}".format(output, x, y))
        self.memory[output] = x * y
    
    def jumpOnNonZero(self, value:int, newPosition:int ):
        if(value != 0):
            # print("jumping to {0}".format(value))
            self.cursor = newPosition

    def jumpOnZero(self, value:int, newPosition:int ):
        if(value == 0):
            # print("jumping to {0}".format(value))
            self.cursor = newPosition

    def equalsTo(self, x:int , y: int, output:int):
        value = int(x == y)
        self.memory[output] = value


    def lessThan(self, x:int , y: int, output:int):
        value = int(x < y)
        self.memory[output] = value

    def store(self, output:int):
        self.memory[output] = self.statusCode

    def output(self, output: int ):
        print("- Diagnostic Code {0} - ".format(output))

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
        "5" : {
            "action": jumpOnNonZero,
            "param": 2
        },
        "6" : {
            "action": jumpOnZero,
            "param": 2
        },
        "7" : {
            "action": lessThan,
            "param": 3
        },
        "8" : {
            "action": equalsTo,
            "param": 3
        },
    }

    def process(self, instruction:str, params: list):
        args = []
        modes = []
        opcode = instruction[-1:]

        modes = (instruction.zfill(5))[:-2]
        modes = modes[::-1]
        for index, param in enumerate(params):
            if modes[index] == "0" and opcode != "3":
                args.append(self.memory[param])
            else :
                args.append(param)

        self.operate(opcode, args,params)
        # print ("Instruction {0} with params {1} and modes {2} at {3}".format(instruction, args,modes,  params))   

    def operate(self, opcode:str, args:list, params:list):
        
        if len(params) == 3:
            self.operations[opcode]["action"](self, args[0], args[1], params[2])
        elif len(params) == 2:
            self.operations[opcode]["action"](self, args[0], args[1])
        else:
            self.operations[opcode]["action"](self, output = args[0])    
            

    def run (self):
        while self.cursor < len(data):
            instruction = str(data[self.cursor])
            if instruction == "99": 
                break
            
            opcode = instruction[-1:]
            nbOfParams = self.operations[opcode]["param"]
            params = data[self.cursor + 1 :self.cursor + nbOfParams + 1] 
        
            nextPosition =self.cursor + nbOfParams + 1
            self.cursor = nextPosition
            self.process(instruction, params)

if __name__== "__main__":

    response = requests.get("https://adventofcode.com/2019/day/5/input", headers={"Cookie":"session=53616c7465645f5f5966fe32801f52f3ccdcfda4336dfce8c64ce2f469c48c2688e46a073403cda4de928b6ae1a21e2d"})

    if response.status_code == 200:
        data = response.text.split(",")

        # convert to int
        data = [int(i) for i in data]

        # data = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]

        computer = Computer(data, 5)
        computer.run ()
        # answer part 1 was 16209841
        # answer part 2 was 8834787
    else :
        print("Could not retrieve data")


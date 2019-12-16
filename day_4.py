


from itertools import groupby

rules = [
    lambda s: any(s[i] == s[i+1] for i in range(0, len(s) - 1)),
    lambda s: all(s[i] <= s[i+1] for i in range(0, len(s) - 1)),
    lambda s: any(len(list(g)) == 2 for _, g in groupby(s))
]

if __name__== "__main__":
    index: int = 307237
    end: int = 769058
    count: int = 0
    array =[]

    while index <= end:
        ruleValid = False
        for rule in rules:
            ruleValid = rule(str(index))
            if not ruleValid :
                break
        if ruleValid:
            count += 1
        index += 1
    print ("the number of possible password is {0}".format(count))
        
   
    


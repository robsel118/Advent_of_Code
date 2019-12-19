
def setOrbitingPlanets(relations, planetName, level):
    children = []
    currentLevel =  level + 1
    for orbit in relations:
        if planetName == orbit["parent"] :
            orbitingPlanetName = orbit["child"]
            orbitingPlanet = {
                "parent":orbitingPlanetName,
                "level": currentLevel,
                "children": setOrbitingPlanets(relations, orbitingPlanetName, currentLevel) 
            }
            children.append(orbitingPlanet)
    return children

def countOrbit(planet):
    temp = 0
    for child in planet["children"]:
        print(child["level"])
        temp += child["level"]
        temp += countOrbit(child)
    return temp

if __name__== "__main__":
    with open(r"./input_6.txt") as file:
        data = file.read().splitlines()
        # print (data)

        relations = []
        root = "COM"
        for path in data:
            planets = path.split(")")
            relations.append({
                "parent": planets[0],
                "child": planets[1]
            })
        print(len(relations))

        orbitMap = {
            "parent": root,
            "level": 0,
            "children": []
        }
        orbitMap["children"] = setOrbitingPlanets(relations, root, 0)

        print(countOrbit(orbitMap))
        

                        
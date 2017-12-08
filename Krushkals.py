import pprint


def getParseInput():
    #function to take inputGraph from the user and also parse the int values
    print("Input the edges of the Graph in the form of 'VERTICE' 'VERTICE' 'COST' \nInput q after finishing the input")
    inputString = "test"
    inputGraph = [[]]
    inputGraph.pop(0)
    while(True):
        inputString = input()
        #exit condition
        if(inputString == 'q'):
            break

        #get input Graph from user and store in 2D list
        stringInput = inputString.split()

        #Parse cost into int and add it to the original list
        inputGraph.append( [stringInput[0], stringInput[1], int(stringInput[2])] )

    return(inputGraph)

def removeLoop(inputGraph):
    #function to remove loops in the Graph
    count = 0
    for row in inputGraph:
        if(row[0] == row[1]):
            inputGraph.pop(count)
        count+=1

    return(inputGraph)

def sortVertices(inputGraph):
    #function to sort the internal vertices that is, example if b a 2 then make it a b 2
    for row in inputGraph:
        if(row[0] > row[1]):
            temp = row[1]
            row[1] = row[0]
            row[0] = temp

    return(inputGraph)

def sortGraphByVertices(inputGraph):
    #incomplete
    #https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
    #sort the Graphs lexcicographically of their first vertices
     inputGraph = sorted(inputGraph, key = lambda x: (x[0], x[1], x[2]) )

     return(inputGraph)

def removeParallelEdges(inputGraph):
    #incomplete
    #function to remove multiple egdes from the same pair of veritces
    inputGraph = sortGraphByVertices(inputGraph)
    inputGraph
    newGraph = []
    # while inputGraph:








if __name__ == '__main__':
    #Take input from user
    inputGraph = getParseInput()
    pprint.pprint(inputGraph)

    #remove loops
    inputGraph = removeLoop(inputGraph)

    #remove multiple egdes between the same verices pair
    inputGraph = sortVertices(inputGraph)

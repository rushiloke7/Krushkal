mylist = [[1,2],[3,4],[1,2],[5,6],[6,7]]
newList = []
i = 0

while mylist:

    if not (mylist[i] in newList):
        newList = mylist.pop(i)
        print(newList)
    else:
        mylist.pop(i)
    i += 1

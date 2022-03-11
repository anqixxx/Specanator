from app import app

class memory:
    def __init__(self):
        self.highestmem = 0
    def getmemory(self):
        return self.highestmem
    def setmem(self, value):
        self.highestmem = value

userMemory = memory()

#mimics code that will be in main
# create list of apps in main, iterate through all to add the total storage
applist = set()
x = app("minecraft")
applist.add( x )
y = app("same")
applist.add( y )

# finds total storage from all the apps given
for val in applist:

    test = val.getram()
    prev = userMemory.highestmem

    if test > int(prev) : userMemory.setmem(test)

from pydoc import importfile
from app import app


class storage:
    def __init__(self):
        self.totalstorage = 10
    def addstorage(self, value):
        print(self.totalstorage)
        self.totalstorage += value
        print(self.totalstorage)
    def getstorage(self):
        return self.totalstorage

userStorage = storage()

#mimics code that will be in main
# create list of apps in main, iterate through all to add the total storage
applist = set()
x = app("minecraft")
applist.add( x )
y = app("same")
applist.add( y )

# finds total storage from all the apps given
for val in applist:
    print( val.getgpu() )
    userStorage.addstorage( val.getssd() )
    print( "storage" + str( userStorage.totalstorage )) 
    

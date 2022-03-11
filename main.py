from app import app
import sys, select, os

applist = set()

while True:
    appName = input("Enter App:")
    if not appName:
        break
    appName = appName.lower()
    newApp = app( appName )
    applist.add(newApp)

for val in applist:
    print( val.name )
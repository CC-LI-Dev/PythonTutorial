from gamegrid import *
from random import *

class Alien(Actor):
    def __init__(self):
        Actor.__init__(self,"sprites/alien.png")
    
    def act(self):
        self.move()
    
def destroyAlien(e):
    location = toLocationInGrid(e.getX(), e.getY())
    actor = getOneActorAt(location)
    if actor != None:
        removeActor(actor)
    refresh()

class Spaceship(Actor):
    def __init__(self):
        Actor.__init__(self, "sprites/car2.png")
        
    def act(self):
        delay(1000)
        self.move()


makeGameGrid(20, 16, 60, Color.red, "/home/cchristoph/Downloads/TigerJython/space-invaders-extreme-1.png", mousePressed=destroyAlien)

setSimulationPeriod(800)
show()
doRun()

while not isDisposed():
    ship = Spaceship()
    addActor(ship, Location(10,16))
    alien = Alien()
    addActor(alien, Location(randint(0,20),0),90)
    delay(400)
    


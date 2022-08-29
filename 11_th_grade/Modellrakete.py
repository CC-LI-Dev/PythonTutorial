import tkinter as tk
from math import sin
from math import radians
from math import log
heightdegree = float(input("Geben sie den gemessenen Höhenwinkel an:"))
diststart = float(input("Geben sie die Entfernung zum Startplatz an:"))
pressurestart = float(input("Geben sie den Druck am Startort ein:"))
pressureend = float(input("Geben sie den Druck am Endort ein:"))

# conversion of values
heightrad = radians(heightdegree)

# calculation with angle

heightrocketangfin = sin(heightrad)*diststart

# calculation with pressure

#heightrocketpres1 = (log(pressurestart)*1013.25)/(log(1013.25)*1.29*9.81)
#heightrocketpres2 = (log(pressureend)*1013.25)/(log(1013.25)*1.29*9.81)

heightrocketpres1 = -((log(pressurestart/1013.25)*1013.25)/1.29*9.81)
heightrocketpres2 = -((log(pressureend/1013.25)*1013.25)/1.29*9.81)
print(heightrocketpres1)
print(heightrocketpres2)
heightrocketpresfin = heightrocketpres2 - heightrocketpres1
if heightrocketpresfin == 0:
    print("Keine Höhe erreicht.")
    quit()
# percentage of difference
 
if heightrocketpresfin > heightrocketangfin:
    percentdif = (heightrocketpresfin-heightrocketangfin)/heightrocketangfin * 100
elif heightrocketangfin > heightrocketpresfin:
    percentdif = (heightrocketangfin-heightrocketpresfin)/heightrocketpresfin * 100

# output

print("Die Höhe in Abhänigkeit der Entfernung vom Startplatz und des Höhenwinkels beträgt:", heightrocketangfin, "m.")
print("Die Höhe in Abhänigkeit vom Druck beträgt", heightrocketpresfin,"m.")
print("Die prozentuale Differenz beider Werte beträgt:", percentdif, "%.")

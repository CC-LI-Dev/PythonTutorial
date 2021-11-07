from math import sin
from math import radians
from math import log
heightdegree = float(input("Geben sie den gemessenen Höhenwinkel in Grad an:"))
diststart = float(input("Geben sie die Entfernung zum Startplatz an:"))
pressurestart = float(input("Geben sie den Druck am Startort in hPa ein:"))
pressureend = float(input("Geben sie den Druck am Endort in hPa ein:"))

# conversion of values
heightrad = radians(heightdegree)

# calculation with angle

heightrocketangfin = sin(heightrad)*diststart
heightrocketangfin = round(heightrocketangfin, 2)
# calculation with pressure

#heightrocketpres1 = (log(pressurestart)*1013.25)/(log(1013.25)*1.29*9.81)
#heightrocketpres2 = (log(pressureend)*1013.25)/(log(1013.25)*1.29*9.81)

heightrocketpres1 = -((log(pressurestart/1013.25)*1013.25)/1.29*9.81)
heightrocketpres2 = -((log(pressureend/1013.25)*1013.25)/1.29*9.81)
print(heightrocketpres1)
print(heightrocketpres2)
heightrocketpresfin = heightrocketpres2 - heightrocketpres1
heightrocketpresfin = round(heightrocketpresfin, 2)
if heightrocketpresfin == 0:
    print("Keine Höhe erreicht.")
    quit()
# percentage of difference

percentdif = (heightrocketpresfin-heightrocketangfin)/heightrocketangfin * 100
percentdif = abs(percentdif)
percentdif = round(percentdif, 2)
# output

print("Die Höhe in Abhänigkeit des Höhenwinkels beträgt:", heightrocketangfin, "m.")
print("Die Höhe in Abhänigkeit vom Druck beträgt", heightrocketpresfin,"m.")
print("Die prozentuale Differenz beider Werte beträgt:", percentdif, "%.")

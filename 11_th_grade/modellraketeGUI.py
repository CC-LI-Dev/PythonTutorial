import tkinter as tk
from math import sin
from math import radians
from math import log
def inputcom():
    heightdegree = float(inputangle.get())
    diststart = float(inputdist.get())
    pressurestart = float(inputprest.get())
    pressureend = float(inputpreend.get())

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
    tk.Label(mask, text="Höhe über Höhenwinkel:").grid(row=7)
    tk.Label(mask, text="m").grid(row=7, column=2)
    outputangh = tk.Entry(mask)
    outputangh.grid(row=7, column=1)
    tk.Label(mask, text="Höhe über Druck:").grid(row=8)
    tk.Label(mask, text="m").grid(row=8, column=2)
    outputpreh = tk.Entry(mask)
    outputpreh.grid(row=8, column=1)
    tk.Label(mask, text="Prozentuale Abweichung:").grid(row=9)
    tk.Label(mask, text="%").grid(row=9, column=2)
    outputperd = tk.Entry(mask)
    outputperd.grid(row=9, column=1)
    outputangh.insert(0, heightrocketangfin)
    outputpreh.insert(0, heightrocketpresfin)
    outputperd.insert(0, percentdif)

mask = tk.Tk()
mask.title("Höhenberechnung")
tk.Label(mask, text="Höhenwinkel in Grad:").grid(row=0)
tk.Label(mask, text="Entfernung vom Startplatz:").grid(row=1)
tk.Label(mask, text="Druck auf der Starthöhe in hPa:").grid(row=2)
tk.Label(mask, text="Druck auf Endhöhe in hPa:").grid(row=3)
inputangle = tk.Entry(mask)
inputangle.grid(row=0, column=1)
inputdist = tk.Entry(mask)
inputdist.grid(row=1, column=1)
inputprest = tk.Entry(mask)
inputprest.grid(row=2, column=1)
inputpreend = tk.Entry(mask)
inputpreend.grid(row=3, column=1)
tk.Button(mask, text="Beenden", command=mask.quit).grid(row=11, column=0, sticky=tk.W, pady=4)
tk.Button(mask, text="Senden", command=inputcom).grid(row=5, column=1, sticky=tk.W, pady=4)
mask.mainloop()

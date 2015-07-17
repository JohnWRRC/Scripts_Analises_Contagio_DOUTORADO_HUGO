import grass.script as grass
import os
p=grass.mlist_grouped ('rast', pattern='mapa*') ['PERMANENT']
for i in p:
    #print i
    grass.run_command("r.neighbors",input=i,out=i+"_dila_25m",method='maximum',size=11)
    

    
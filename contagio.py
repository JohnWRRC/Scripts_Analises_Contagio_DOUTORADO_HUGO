#!/c/Python25 python
#import sys, os, numpy #sys, os, PIL, numpy, Image, ImageEnhance
import grass.script as grass
from PIL import Image
import wx
import random
import re
import time
import math
#from rpy2 import robjects
from datetime import tzinfo, timedelta, datetime
import win32gui
from win32com.shell import shell, shellcon
import os
import unicodedata
import math
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

x=grass.read_command('r.stats',input="all_landscapes_r5_img_rec")
grass.run_command("g.region",rast="all_landscapes_r5_img_rec")
y=x.split('\n')
del y[-1]
del y[-1]
#print y

for i in y:
    j=i
    #print j
    name='000000'+j
    name=name[-6:]
    #print name
    expressao1="mapa_"+name+"=if(all_landscapes_r5_img_rec=="+j+",all_landscapes_r5_img_rec,0)"
    print expressao1
    grass.mapcalc(expressao1, overwrite = True, quiet = True)




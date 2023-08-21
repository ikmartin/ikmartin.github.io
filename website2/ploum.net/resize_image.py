#!/bin/python
from PIL import Image
from pathlib import Path
import os
maxsize = 800
dir = "/home/ploum/dev/gemlog/files/"
for root,dirs,files in os.walk(dir):
    for fi in files:
        p = Path(dir+fi)
        if p.exists() and (fi.endswith(".jpg") or fi.endswith(".jpeg") or fi.endswith(".png")):
            #f = open(dir+fi)
            im = Image.open(dir+fi)
            width,height = im.size


            if width > maxsize or height > maxsize:
                if width > height:
                    new_height = int((height/width)*maxsize)
                    newsize = (maxsize,new_height)
                else:
                    new_width = int((width/height)*maxsize)
                    newsize = (new_width,maxsize)
                print("oldsize : ",width,"x",height, " for %s"%fi)
                output = im.resize(newsize)
                output.save(dir+fi)
            im.close()

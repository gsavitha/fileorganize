import os
import json
files={}
ext={}
byteconv=1024.0*1024
#Uncomment the below line and comment the above line if you believe 1MB=1000B, you heathen.
#byteconv=1000.0*1000.0
for dpath, dnames, fnames in os.walk(os.path.expanduser("~")):
    ##Excluding hidden files
    dnames[:] = [d for d in dnames if not d.startswith('.')]
    for file in fnames:
            fn=os.path.join(dpath, file)
            try:
                files[fn]=os.path.getsize(fn)
            except:
                continue
for dpath, dnames, fnames in os.walk(os.path.join(os.path.expanduser("~"),"Desktop")):
    for file in fnames:
            fn=os.path.join(dpath, file)
            try:
                e=os.path.splitext(fn)[1]
                if e not in ext:
                    ext[e]=list()
                ext[e].append([dpath,file])
            except:
                continue
i=0
for x in sorted(files, key=files.get, reverse=True):
    i+=1
    if(i==10):
        break
    print( x,files[x]/byteconv)
for e in ext:
    ##Ignoring All Shortcuts.
    if e==".lnk":
        continue
    dir=os.path.join(os.path.expanduser("~/Documents"),e.replace(".","").upper())
    os.makedirs(dir, exist_ok=True)
    for x in ext[e]:
        os.rename(os.path.join(x[0],x[1]),os.path.join(dir,x[1]))
##Removing Empty Directories.
for dpath, dnames, fnames in os.walk(os.path.join(os.path.expanduser("~"),"Desktop"),topdown=False):
    for dirs in dnames:
        try:
            os.rmdir(os.path.join(dpath,dirs))
        except:
            continue

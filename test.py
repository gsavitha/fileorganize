import os
for dpath, dnames, fnames in os.walk('/home/savitha/Desktop'):
    for file in fnames:
            fn=os.path.join(dpath, file)
            print fn

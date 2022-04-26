
import hashlib
import urllib.request
import shutil

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

origfile = "./halfcheetah_medium-v2.hdf5"
url = "http://rail.eecs.berkeley.edu/datasets/offline_rl/gym_mujoco_v2/halfcheetah_medium-v2.hdf5"
# message = hash_file(myfile)
curfile = origfile
urllib.request.urlretrieve(url, origfile)
currenthash = hash_file(origfile)
hashdict = {}
ct=0

while(currenthash not in hashdict.values()):
    print(hashdict)
    hashdict[curfile] = currenthash
    ct+=1
    curfile = origfile + str(ct)
    urllib.request.urlretrieve(url, curfile)
    currenthash = hash_file(curfile)

shutil.move(curfile, origfile)
import pymongo
from pymongo import MongoClient
import gridfs
from PIL import Image

cluster = MongoClient("mongodb+srv://team2:179g@cluster0.fm94y.mongodb.net/Impostergram?retryWrites=true&w=majority") #connects to our mongodb server
db = cluster["Impostergram"] #specifies the impostergram cluster
collection = db["Photos"] #specifies the photos collection
fs = gridfs.GridFS(db) 

print("opening test text")
data1 = open("testFS.txt",'rb')
print("putting text into db")
txt_id=fs.put(data1,filename="testtxt")
print("closing txt file")
data1.close()
print("saving txt id")
out_data=fs.get(txt_id).read()

print("opening output txt")
output =open("txtresult.txt",'wb')
print("writing to outputtxt")
output.write(out_data)
print("closing file")
output.close()


data2 = open("testimgFS.jpg",'rb')
img_id=fs.put(data2,p_id="p1")
data2.close()
out_data=fs.get_version(p_id="p1").read()

output=open("imgresult.jpg",'wb')
output.write(out_data)
output.close





#post= {"_id":"p1"}


#collection.insert_one(post)

#result = collection.find({"_id":"p1"})

#for x in result:
    #print(x)
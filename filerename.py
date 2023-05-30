import os
path = input('Enter the path:- ') #/Users/ruvi/Desktop/FCT/files
print(path)

print(os.listdir(path))

def main():
    i=1
    for filename in os.listdir(path):
        newname = path+"flower"+str(i)+'.jpeg'
        oldname = path+filename
        os.rename(oldname,newname)
        i+=1

main()
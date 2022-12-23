import shutil

source = input("please enter the address and the full name of the of the zpl file in correct format :")
dst = input("please enter destination :")
desty = dst.replace("\\","/")
f = open(source, "r", encoding="utf8")



def Read(f): #reads the file line by line 
    something = []
    for x in f:
        temp = x.replace("\\","/")
        something.append(temp)
    return something

def PS (L) : #gathers lines that contains a path
    pathLines = []
    for x in L :
        if "src" in x:
            pathLines.append(x)
    return pathLines

def slice (target): #will pull out raw path to the file
    avalesh = []
    final = []
    county = 0
    for x in target :
        avalesh.append(x[18:])
        temp = avalesh[county]
        lastIndex = temp.find("\" albumTitle=")
        final.append(temp[:lastIndex])
        county+=1
    return final

def dupper (srcList,dst):# this will duplicate the file to your desired destination
    counter = 0
    sucsess = 0
    fails = 0
    for x in srcList :
        temp = x
        try:
            shutil.copy(temp, dst)
            print(f"{counter} file has been copied !")
            sucsess = sucsess + 1
        except:
            print(f"file number{counter} with address of {temp} does not exist")
            fails = fails + 1
        counter= counter + 1 
    
    print(f"total of {sucsess} musics has been exported successfully and {fails} musics are mising.")


paths = slice(PS(Read(f)))
dupper(paths,desty)

input(
"""
***************************************
* you may kill the terminal safely !!!*
***************************************
""")
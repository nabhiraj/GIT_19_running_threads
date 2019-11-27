import threading 
import hashlib
import os

def md5_func(num,f_name):
    fp=open(f_name,"rb")
    fp1=open("/home/praveena/Desktop/sam","ab")
    ele=fp.read(524288*num)
    print(fp.tell())
    ele1=fp.read(524287)
    print(fp.tell())
    fp1.write(ele1)
    val=hashlib.md5(ele1).hexdigest()
    print(val)
    fp.close()
    fp1.close()

if __name__ == "__main__": 
    f_name="/home/praveena/important/os/assignment_2/text.txt"
    
    statinfo = os.stat('/home/praveena/important/os/assignment_2/text.txt')
    size=statinfo.st_size
    print(size)
    if size>100:
        #512kb = 524288
        no_of_threads=int(size/524288)
        if size%524288 != 0:
            no_of_threads+=1
        for i in range(0,no_of_threads):
            t1 = threading.Thread(target=md5_func, args=(i,f_name,))
            t1.start()
            t1.join()
    
            

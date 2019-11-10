import sys
import os
import difflib
import hashlib#for calculating md5hash
#taking command line arguments in python
def current_files():
    #check all the file exept from mygit
    res=[]
    forbiden_path=os.getcwd()+'/.mygit'
    for root,dirs,files in os.walk(os.getcwd()):
        temp_root=root
        if root!=forbiden_path:
            for i in files:
                #print(temp_root+'/'+i)
                res.append(temp_root+'/'+i)
    return res
  
def extract_previous_commit_info():
     #this will return list of file name and there hash and ther diff file n.o
    master_file=open('.mygit/master_file.txt','r')
    current_commit_num=master_file.read()
    current_commit_file_name='.mygit/commit_'+current_commit_num
    print('printing the name of the file ',current_commit_file_name)
    print('number of charecters in the file name is ',len(current_commit_file_name))
    current_commit_file=open(current_commit_file_name,'r')
    num_of_file=current_commit_file.readline()#reading the number of file.
    my_map={}
    for i in range(int(num_of_file)):
        #this loop will run num_of_file times.
        key=current_commit_file.readline()		 #**sequence num of commit
        value_h=current_commit_file.readline()	 #**name of that file
        value_d=current_commit_file.readline()   #**difference index
        value=(value_h,value_d)
        my_map[key]=value
    master_file.close()
    current_commit_file.close()#closing both the opened file.
    return my_map

def file_changed():
    prev_map=extract_previous_commit_info()
    cf=current_files()
    changed=[]
    no_changed=[]
    for e_f in cf:
        if e_f in prev_map.keys():
            e_f_hash_value=hashlib.md5(e_f).hexdigest()
            if e_f_hash_value==prev_map[e_f][0]:
                no_changed.append(e_f)
            else:
                changed.append(e_f)
            pass
        else:
            changed.append(e_f)
    t=(changed,no_changed)
    return t

def satus():
    t=file_changed()
    changed_file=t[0]
    not_changed_file=t[1]
    print('file which have changed')
    for i in changed_file:
        print(i)
    print('file which have to change')
    for i in not_changed_file:
        print(i)
        
def add(x):
	forbiden_path=os.getcwd()+'/.mygit'
	for root,dirs,files in os.walk(os.getcwd()):
		temp_root=root
		if root!=forbiden_path:
			for i in files:
				if(x==i):
					#**check whether the file is different from the commited one by comparing md5 
					rf=open('.mygit/addlist_unique.txt','r')
					#print(temp_root+'/'+i)
					
					for j in enumerate(rf):		#**loop to check whether any previous adds of same file are there or not
						if j[1] == temp_root+'/'+i+'\n':
							print("Already exist")
							#** write code to check whether it is different from previously added file
							#** write code which overwrites previous temp_diff
							return 
					rf.close()
					
					af=open('.mygit/addlist_unique.txt','a')
					af.write(temp_root+'/'+i+'\n')     #af add file path if it has not been added before
					tempd=open('.mygit/temp_diff'+i+'.txt','w')
					'''
					-code to open the previous committed/added file and calculate difference
					-storing the difference temporarily in temp_diff which will be permanently saved while committing
					'''
					af.close()
					return
	print("File not found...")		          
					

#execuion of code start from this file.
a=sys.argv
if a[1]=='init':
    if len(a)!=2:
        print("not correct number of arguments")
    else:
        print('correct implementation starts from here')
        #we need to create a master file
        os.mkdir('.mygit')
        master_file=open('.mygit/master_file.txt','w')
        master_file.write('0')
        #now we have to do the zero't commit
        zeroth_commit=open('.mygit/commit_0','w')
        zeroth_commit.writelines('0')
        current_diff_counter=open('.mygit/diff_counter','w')
        current_diff_counter.write('1')#take the number out and then increment
        master_file.close()
        zeroth_commit.close()
        current_diff_counter.close()
elif a[1]=='status':
    print('calling the status code')
    satus()
   
elif a[1]=='add':
	print('add being called')
	print(a[2])
	add(a[2])

current_files()
     

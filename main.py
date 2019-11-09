import sys
import os
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
     #this will return list of file name and there hast and ther diff file n.o
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
        key=current_commit_file.readline()
        value_h=current_commit_file.readline()
        value_d=current_commit_file.readline()
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
     
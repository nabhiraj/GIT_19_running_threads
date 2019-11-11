import sys
import os
import os.path
import difflib
import hashlib#for calculating md5hash
#taking command line arguments in python
import difflib
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
    current_commit_file=open(current_commit_file_name,'r')
    num_of_file=current_commit_file.readline()#reading the number of file.
    my_map={}
    for i in range(int(num_of_file)):
        #this loop will run num_of_file times.
        key=current_commit_file.readline()       #complete path of the file
        print('the path of the file is ',key)
        value_h=current_commit_file.readline()   #hash of the file
        print('the hash of the file is ',value_h)
        value_d=current_commit_file.readline()   #diff index of the file.
        print('the diff index of the file is ')
        value=(value_h,value_d)
        my_map[key]=value
    master_file.close()
    current_commit_file.close()#closing both the opened file.
    return my_map

def extract_previous_add_info():
    only_add_file=open('.mygit/addlist_unique.txt')
    num_co_file=open('.mygit/myfile_counter.txt','r')
    number_of_entry=num_co_file.read()
    number_of_entry=int(number_of_entry)
    my_map={}
    for i in range(number_of_entry):
        key=only_add_file.readline()
        print('the path of the file is ',key)
        value_h=only_add_file.readline()
        print('the hash of the file is ',value_h)
        value_d=only_add_file.readline()
        print('the temp diff index of the file is ',value_d) 
        value=(value_h,value_d)
        my_map[key]=value
    only_add_file.close()
    num_co_file.close()
    return my_map

def file_changed():
    if os.path.exists('.mygit/addlist_unique.txt'):
        print('code should not be here')
        prev_map=extract_previous_add_info()
    else:
        print('code should be here')
        prev_map=extract_previous_commit_info()#returns a map wiht following structure. 
    cf=current_files()#return complete path of all the files in he directory.
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
    x=os.path.abspath(x)
    my_map=extract_previous_commit_info()
    changed_fil=file_changed()[0]
    add_file_dis=""
    if x in changed_fil:
        if os.path.exists('.mygit/addlist_unique.txt'):
            add_file_dis=open('.mygit/addlist_unique.txt','a')
        else:
            add_file_dis=open('.mygit/addlist_unique.txt','w')
            mytempt=open('.mygit/myfile_counter.txt','w')
            mytempt.writelines('0')
            mytempt.close()
        #hash
        #diff index after creating the diff file.
        current_diff_counter=open('.mygit/diff_counter','r')#does rw works.
        diff_val=int(current_diff_counter.readline())+1
        current_diff_counter.close()
        current_diff_counter=open('.mygit/diff_counter','w')
        current_diff_counter.write(str(diff_val))
        current_diff_counter.close()
        add_file_dis.writelines(x+'\n') # writing the path of the file tuple 1.
        hash_val=hashlib.md5(open(x,'rb').read()).hexdigest() 
        add_file_dis.writelines(hash_val+'\n')
        if x in my_map.keys():
            print('the file already exist in previous commit')
            print('this will be implimented in future')
            print('all diff to the current add will be with respect to the prevous/current commit')
        else:
            #base case.
            #diff increment.
            temp_diff_file_name=".mygit/temp"+"diff"+str(diff_val)
            temp_diff_file=open(temp_diff_file_name,'w')
            xx=open(x,'r')
            temp_diff_file.write(xx.read())
            xx.close()
            temp_diff_file.close()
            #my_file_counter ko increment karna hai.
            temp_counter_file=open('.mygit/myfile_counter.txt','r')
            t=int(temp_counter_file.read())
            t=t+1
            temp_counter_file.close()
            temp_counter_file=open('.mygit/myfile_counter.txt','w')
            temp_counter_file.write(str(t));
            temp_counter_file.close()
            add_file_dis.writelines(str(diff_val-1)+'\n')
            
    else:
        print('there is no change in file ',x)
        
        
    add_file_dis.close()
                    
                  
                    

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

#current_files()
     

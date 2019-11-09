import sys
import os
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
    current_commit_file_name='commit_'+current_commit_num
    current_commit_file=open(current_commit_file_name,'r')
    num_of_file=current_commit_file.readline()
    ret=[]
    for i in range(num_of_file):
        #this loop will run num_of_file times.
        temp=[]
        temp.append(current_commit_file.readline())
        temp.append(current_commit_file.readline())
        ret.append(temp)
    return ret
def file_changed():
    #compute the files which we have changed.
    
    
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
    print('printing from here',current_files())
    #now we have to check which all files have changes from the previous commit
    
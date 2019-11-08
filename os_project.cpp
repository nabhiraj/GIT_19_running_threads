#include<stdio.h>
#include<unistd.h>
#include<bits/stdc++.h>
#include<string.h>
#define MAX 100

using namespace std;

class info_of_dir{
	public:
		int n;//number of files in the directory
		string* name_of_file;
		char** hash_of_each_file;
	//method..
	void run_the_routine(){
		//check each and every file in the directory.
	}
}
int check(char one[MAX],char two[MAX],char three[MAX])
{
	if(strcmp(one,"git")==0)
	{
		if(strcmp(two,"init")==0)
		{
			//create a master file which will keep record of current commit version -1
			//name of the master file is master
			//create a directory my_git
			//inside this file master_record.txt
			//      field current commit=-1
			return 1;
		}
		else if(strcmp(two,"add")==0)
		{
			return 2;
		}
		else if(strcmp(two,"status")==0)
		{
			return 3;
		}
		else if(strcmp(two,"commit")==0)
		{
			return 4;
		}
		else if(strcmp(two,"diff")==0)
		{
			return 5;
		}
		else if(strcmp(two,"rollback")==0)
		{
			return 6;
		}
		else if(strcmp(two,"log")==0)
		{
			return 7;
		}
		else if(strcmp(two,"retrieve")==0)
		{
			return 8;
		}
	}
	else
	{
		cout<<"Enter correct command"<<endl;
	}
}
void git_init()
{
	cout<<"git_init";
}
void git_add()
{
	cout<<"git_add";
}
void git_status()
{
	cout<<"git_status";
}
void git_commit()
{
	cout<<"git_commit";
}
void git_diff()
{
	cout<<"git_diff";
}
void git_roll_back()
{
	cout<<"git_roll_back";
}
void git_log()
{
	cout<<"git_log";
}
void git_retrieve()
{
	cout<<"git_retrieve";
}
int main(int argc, char ** argv)
{
	int res=check(argv[1],argv[2],argv[3]);
	if(res==1)
	{
		git_init();
	}
	else if(res==2)
	{
		git_add();
	}
	else if(res==3)
	{
		git_status();
	}
	else if(res==4)
	{
		git_commit();
	}
	else if(res==5)
	{
		git_diff();
	}
	else if(res==6)
	{
		git_roll_back();
	}
	else if(res==7)
	{
		git_log();
	}
	else if(res==8)
	{
		git_retrieve();
	}
	return 0;
}

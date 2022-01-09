import sys
import os
def readfile(f):
    try:
        fr=open(f,"r")
        r=fr.readlines()
        r.sort()
        fr.close()
        return r
    except:
        fw=open(f,"w")
        fw.close()

def writefile(f,txt):
    try:
        fw=open(f,"a")
    except:
        fw=open(f,"w")
    fw.write(txt)
    fw.close()
    
def clearfile(f):
    fc=open(f,"r+")
    fc.truncate(0)
    fc.close()

def show_help():
    helps=\
        """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(helps.encode('utf8'))

def main():
    command = sys.argv[1:]
    if len(command)>=1:
        if command[0]=="add":
            try:
                if command[1] and command[2]:
                    data="{} {}\n".format(command[1],command[2])
                    writefile("task.txt",data)
                    print('Added task: "{}" with priority {}'.format(command[2],command[1]),end="")
            except:
                print("Error: Missing tasks string. Nothing added!",end="")
        elif command[0]=="ls" and len(command)==1:
            try:
                x=readfile("task.txt")
                st = ''
                for idx,i in enumerate(x):
                    s=i.split()
                    txt=" ".join(s[1:])
                    sys.stdout.buffer.write("{}. {} [{}]\n".format(str(idx+1),txt,s[0]).encode('utf8'))
            except:
                print("There are no pending tasks!")
        elif command[0]=="del":
            try:
                if len(command)>1:
                    idx = int(command[1])
                    if idx!=0:
                        d=readfile("task.txt")
                        del d[idx-1]
                        d="".join(d)
                        clearfile("task.txt")
                        writefile("task.txt",d)
                        print(f"Deleted task #{idx}",end="")
                    else:
                        print(f"Error: task with index #0 does not exist. Nothing deleted.",end="")
                else:
                    print(f"Error: Missing NUMBER for deleting tasks.",end="")
            except:
                print(f"Error: task with index #{idx} does not exist. Nothing deleted.",end="")
        elif command[0]=="done":
            try:
                idx_done = int(command[1])
                d=readfile("task.txt")
                if idx_done <= len(d) and idx_done!=0:
                    data="{}".format(d[idx_done-1])
                    writefile("completed.txt",data)
                    del d[idx_done-1]
                    d="".join(d)
                    clearfile("task.txt")
                    writefile("task.txt",d)
                    print("Marked item as done.",end="")
                else:
                    print(f"Error: no incomplete item with index #{idx_done} exists.",end="")
            except:
                print("Error: Missing NUMBER for marking tasks as done.",end="")
        elif command[0]=="report" and len(command)==1:
            try:
                d=readfile("task.txt")
                txt="Pending : {}\n".format(str(len(d)))
                for idx,i in enumerate(d):
                    s=i.split()
                    t=" ".join(s[1:])
                    txt+="{}. {} [{}]\n".format(str(idx+1),t,s[0])
                comp=readfile("completed.txt")
                txt+="\nCompleted : {}\n".format(str(len(comp)))
                for idx,i in enumerate(comp):
                    s=i.split()
                    t=" ".join(s[1:])
                    txt+="{}. {}\n".format(str(idx+1),t)
                sys.stdout.buffer.write(txt.encode('utf8'))
            except Exception as e:
                print("There are no Pending and Completed tasks!",end="")
        elif command[0]=="help" and len(command)==1:
            show_help()
        else:
            show_help()
    else:
        show_help()

if __name__=='__main__':
    main()

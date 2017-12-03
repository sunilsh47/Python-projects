#! /usr/local/bin/python3.5

import subprocess as sp
#import sys

print("Welcome to automation!!!")
#HOST='192.168.56.101'
state='hostname'
while(state!='stop'):
     
     HOST=input("please enter the server IP/hostname: ")
     user=str(input("please enter the username: "))
     if(HOST=='stop'):
          break
#     state=str(input("please input the command which you want to run: "))
     while(state!='change server' or state!='stop'):
           state=str(input("please input the command which you want to run: "))
           if(state=='stop' or state=='change server'):
              break
           ssh_cmd='ssh %s@%s %s' % (user, HOST, state)
           result=sp.Popen(ssh_cmd,shell=True,stdout=sp.PIPE).stdout.read()
           print(result)



import os
import sys
import time



#Login






uname=input("\033[0;32menter user name=-💬-  ")
passwd=""
attempt=0
flag=0
while(attempt!=10000000000):
    passwd=input("\033[0;33menter password- 👁  🔰-🔰-☢️  ")
    if(passwd=="yehia1hacker"):
        flag=1
        break
    else:
        attempt=attempt+1
        if(attempt==10000000000):
            print("you have tried maximum number of time")
if(flag==1):
            print("\033[1;36mwelcome ✅ ",uname.upper () )



# os.system('pause')

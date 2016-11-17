import os   
import json

# nohup python getDeleted.py > my.log 2>&1&
# echo $! > save_pid.txt
    # kill -9 `cat save_pid.txt`
if __name__ == "__main__":
    fname = "shamitabh_mapped_en"
    x = 0
    for i in range(10):
        str1  =  "nohup python userStreaming"+str(x)+".py "+"> my"+str(x)+".log 2>&1&"
        str2 = "echo $! > save_pid"+str(x)+".txt"
        str3 = "kill -9 `cat save_pid"+str(x)+".txt`"
        # print(str1)
        # print(str2)
        print(str3)
        x += 1


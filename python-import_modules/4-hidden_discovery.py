#!/usr/bin/python3
if __name__ == "__main__":
    name = dir("/mnt/hidden_4.pyc")
    for i in name:
        if i[0] != '_':
            print("{}".format(i))
        
    

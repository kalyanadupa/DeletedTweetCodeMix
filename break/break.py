import os   
import json

    
if __name__ == "__main__":
    ip_folder_path = "ipt"
    op_folder_path = "files"
    for content in os.listdir(ip_folder_path):
        fno = 1
        input_file = ip_folder_path+'/'+content
        fn = open("shamitabh_mapped_en.txt")
        op_file = []
        cntnt = "shamitabh_mapped_en.txt"
        for i in range(20):
            op_file.append(op_folder_path+'/'+cntnt[:-4]+str(i+1)+'.json')
        data = json.load(fn)
        for i in range(len(data.keys())):
            fno = i%20
            fo = open(op_file[fno], "a")
            dct = {}
            dct[data.keys()[i]] = str(data[data.keys()[i]]).replace("u\"","\"").replace("u\'","\'")                
            r = json.dumps(dct)
            fo.write(r)
            fo.write("\n")        
            fo.close()

import os   
import json

    
if __name__ == "__main__":
    name = "superbudget_mapped_en"
    ip_folder_path = "etc"
    t = 0
    op_file = name+'.json'
    d3 = {}      
    fo = open(op_file, "w")
    for content in os.listdir(ip_folder_path):
        print content
        if ".json" in content:
            input_file = ip_folder_path+'/'+content
            fn = open(input_file)
            data = json.load(fn) 
            for x in data:
                d3[x] = str(data[x]).replace("u\"","\"").replace("u\'","\'")
    r = json.dumps(d3)
    fo.write(r)        
    fo.close()           


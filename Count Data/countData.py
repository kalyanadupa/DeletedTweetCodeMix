import os   
import json

    
if __name__ == "__main__":
    ip_folder_path = "MappedData"
    t = 0
    for content in os.listdir(ip_folder_path):
        print content
        if ".txt" in content:
            try:
                input_file = ip_folder_path+'/'+content
                fn = open(input_file)
                data = json.load(fn)
                print content,len(data)
                t += len(data)
            except Exception, e:
                print "Error", e
                print content
                pass
    print "Total", t            
            

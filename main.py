import os,shutil 

path = os. getcwd() 
dir_list = os.listdir(path)
print(path)

csv_path = path + '/' + 'csv_file'
if os.path.exists(csv_path) == False:
    os.mkdir(csv_path)
    
txt_path = path + '/' + 'txt_file'
if os.path.exists(txt_path) == False:
    os.mkdir(txt_path)
    
for file in dir_list:
    if '.csv' in file and not os.path.exists(csv_path+'/'+file):
        shutil.move(path+'/'+file,csv_path+'/'+file)
        
    if '.txt' in file and not os.path.exists(txt_path+'/'+file):
        shutil.move(path+'/'+file,txt_path+'/'+file)
    

import os
from datetime import datetime
# print(dir(os)) # to print all the attributes of the modules in which we are working with.
# print(os.getcwd()) #to get the current working directory
# print(os.chdir("G:\workshop\Python"))
# print(os.getcwd())
# os.chdir("G:\workshop\Python\File Handling")
# print(os.listdir("G:\study material\Java Tutorials"))
# os.mkdir("test.txt")
# os.rmdir("test.txt")
# os.rename("test", "moduleos.ts")
# os.rename("ImportOS_Practice.py", "importOS_Practice.py")
# print(os.listdir())
# mod_time = os.stat("importOS_Practice.py").st_mtime
# print(datetime.fromtimestamp(mod_time))
# print(os.walk('G:\Workshop'))
# for dirpath, dirnames, filename in os.walk('G:\Workshop'):
#     print("Current Path : ", dirpath)
#     print("Directories: ",dirnames)
#     print("Files: ", filename)
#     print()
print (True if 'HOME' in os.environ else False)
print(os.environ)
print(os.environ.get('COMPUTERNAME'))
file_path = os.path.join(os.getcwd(), "test.txt")
print(file_path)
print(os.path.isdir('\tmp\test.txt'))
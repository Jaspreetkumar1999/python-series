import os
from datetime import datetime
# os module allowed us to intract with underlined operating system in severaldifferent way for ex we can navigate the file sysyem
# print(dir(os))
#all attribute and methods we can access with this module
# print(os.getcwd())
# to print current working directory
os.chdir("C:/Users/sss/Desktop")
# to change directory simple copy paste location will not work it will show unicode error to handle this we have to make all backward slashes to forword slash
# print(os.getcwd())
# print(os.listdir())
# it will show file and folders stored in the desktop
# os.mkdir('jaspreet')
# to creat new folder or directory
# os.makedirs('jassi11/sub_jassi')
# mkdir and makedirs both are same but if you want to creat few level deep directory then go with makedirs
# os.removedirs('jassi11/sub_jassi')
# # to delete directory of deeper level
# os.rmdir('jaspreet')
# # to remove directory
# os.rename('bootrap tutues','demo_bootstrap')
# to rename the directory
# print(os.stat('bheja'))
# print(os.stat('bheja').st_size)
# my_time=os.stat('bheja').st_mtime
# print(datetime.fromtimestamp(my_time))
# to view information regarding files
os.walk()


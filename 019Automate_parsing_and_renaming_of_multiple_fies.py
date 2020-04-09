# suppose we have multiple video files in unordered way there names are setted randomly we want to arrange them according to ourself
import os
os.chdir('F:/funny/videos')
# print(os.getcwd())
for f in os.listdir():
    # print(f) # to print all files
  # print(os.path.splitext(f)) # for every file it will give tuple there are two values in tuple first is name and second have format ... eg=mp4
    file_name,file_ext = os.path.splitext(f) # we are assigning two variable one is for file name other is for extension
    # print(file_name)
    # print(file_name.split('_')) #splited where _ is presented
    v1, v2, v3, v4, v5 = file_name.split('_') # we got list have 5 members so assign them variable to each one
    # print(v1)
    v1=v1.strip()[1:] # te replace first character
    print(f"{v1}{file_ext}")


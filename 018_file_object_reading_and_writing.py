# # file object
# # to get file object there is built in open command
# # f = open('text.txt','r') # if file is in different directory you have to pass path of that file
# # by default it will open file for reading purposes second argument id for the operation that we want to perform
# # f = open('text.txt','w') # writing
# # f = open('text.txt','a') # appending
# # f = open('text.txt','r+') # read and write
# f = open('text.txt','r')
# # print(f.name) # to print the name
# print(f.mode) # to print mode
# f.close() # if we open the file we have to lose it explicitly
#
# #--------above process is tradional method to dealing with file  but now for most use cases content manager is used to open file

#----------file object we use with keyword
# with open("text.txt",'r') as f:  # it allows us to accessing file in block if we exit the block file automatically closed
#    # f_content= f.read()# only accessing file in the block
#    # f_content = f.readlines() # to read files in lines in list
#  # f_content = f.readline() # to read firstline each time we run it will get next line
#  # print(f_content,end='') # end ='' will end the extra new space left by default when we print through tradional method t
#  # f_content = f.readline()
#  # print(f_content,end='') # nextline
# # print(f.closed) # it returns true
# # print(f.read())
#
# #
#  # for line in f:  #iteration through for loop
#  #    print(line,end='')
#  #  f_content = f.read( 50) # to print first 50 character of our file
#  # #  print(f_content, end='')
#  # #  f_content = f.read(50) # it will print next 50 character
#  # #  print(f_content, end='')
#  #   size_to_read = 10
#  #   f_content = f.read(size_to_read)
#  #   print(f_content, end='')
#  #   f.seek(0) # for second time previously it starts where we left but if want to start at the begining or any position you want
#  #   f_content = f.read(size_to_read)
#  #   print(f_content)
#  #   # print(f.tell()) # it tells us about the size we are going to read
#  #   # while len(f_content)>0:
#  #   #     # here we print our content in blocks we set limit for each time of iteration
#  #   #  print(f_content, end='+')
#  #   #  f_content = f.read(size_to_read)


 #-----------if want to write in file that we had opned in read mode
  # f.write('test') it will show error
# with open('text2.txt','w') as f:  # file opned in write mode. if file doesn't available it will going to creat if it is available then it is going to overwrite
#     # if you don't want to overwrite the file use append method 'a'
#    f.write('test') # it will overwrite our text with test
#
#    # f.write('test') # it will again write test
#    # f.seek(0) # it will write at 0 position or we can say second 'test' will overwrite first 'test'
#    # f.write('test')
#    f.seek(0)
#    f.write('R') # this will overwrite T with R
# with open('text.txt','r') as rf:
#     with open('text_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line) # to copy text.txt > text_copy.txt
with open('img1.jpg','rb') as rf:
    # in dealing with pictures we have to open it in binary mode instead of simple r and w we have to rb and wb
    with open('img1_copy.jpg', 'wb') as wf:
        # for line in rf:
        #     wf.write(line)
        chunk_size = 4096
        rf_chunk =rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
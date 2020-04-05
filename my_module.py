print('imported my module....')
test = 'test string'
def find_index(to_search,target):
    for i,value in enumerate(to_search):
        # enumerate is used to print serial no.
        if target==value:
            return i

    return -1
# courses =['history','technology','bussiness','maths','language']
# for i ,value in enumerate(courses):
#     print(i,value)
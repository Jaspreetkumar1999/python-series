# --------------------------------------------------------------list starts here------------------------------------------------------------------------
courses =['history','english', 'maths','programming']
# print(courses) to print list
# print(len(courses)) to print lenth how many values counting starts from 1 not from 0
# print(courses[2]) to print value stored at particular index
# print(courses[-2]) negative index start from end -1
# print(courses[0:2]) to print stored values starting index is zero and ends at one less than 2( as we gave in syntax)
# print(courses[2:]) starting position index is 2
# print(courses[:3]) to print upto one less index value stopping point one less
# courses.append('art') to add item at the end of list
# courses.insert(3,'art') to insert item at particular location
# courses.insert(3,'art') we can also insert item at negative location it will ad our item by one more negative index
courses1 =['punjabi','hindi']
# courses.insert(0 , courses1)
# print(courses.insert(0 , courses1)) it will not work to inert list
# print(courses) it will add our new list in prev list just as a list but we want to add it as normal items so we use extend method
# print(courses[0][1]) to get the value in 2d list
# courses.extend(courses1) it will add our whole list at the end also considering each item as item in new list
# courses.remove('maths') to remove item just by name
# courses.pop() by default it will pop(remove) item from last
# courses.pop(2) it will remove item from given index
# pop = courses.pop() the property of pop is that it will not only remove it it also return that value we can store it in variable  for further use
# print(pop)
# courses.reverse() to reverse the list
# courses.sort() our items are string so it will sort in the alphabatical order if items are num it wil sort in ascending order
courses2 =['2','3','1','9','4']
# courses2.sort()to sort without changing the orignal one
# hello= sorted(courses)to sort without changing the orignal one
# print(hello)
# print(min(courses)) to print min item in string it will show the first value according to alphabet in number it will show simply min value
# print(max(courses)) to print max
# num = [1,4,3,5,6,7]
# print(sum(num)) to get sum of list but items should be integer
# print(courses.index('maths')) to get index of particular item
# print('maths' in courses) to check whether the value is stored in list
# for item in courses :
#     # print(item) to get items via for loop
# for index, item in enumerate(courses): it will items as well as indexes with items
#        print(index,item)
# for index, item in enumerate(courses, start=1): it will start from 1
#     print(index, item)
# courses_str = ', '.join(courses) it will print our items without the square brackets saperated by , in propper way
# print(courses_str)
# courses_str = ' -' .join(courses)
# new_list = courses_str.split('-') it will convert again into list by adding square bracket around them
# print(new_list)


#            ------------------------------------------------tuple starts here=----------------------------------------------------------------


# tuple same as list but there is one difference that we cannot modify it in programming world we say it imutable it must be inside round bracket
# courses[0]='dsp'
# print(courses)                  example of mutable
# new_courses = courses;
# print(new_courses)
# tuple_1 = ('history1', 'english', 'maths', 'programming')
# tuple_2 = tuple_1
# tuple_1[0]='nas' it will not accept it ......example of immutable
# print(tuple_1)
# print(tuple_2)
#  if you need some thing that you want to modify use list ..or if you want to something like that you dont want to modify ..just want to perform looping or other function which does nt include mutablity use tuple





#                       -------------------------------------------------set start here---------------------------------------------------------------------------------------
# in set we use curly brackets
set_1 ={'history', 'english', 'maths', 'programming'}
# print(set_1) every time when you run it it will show you  in different order. it also remove the duplicates.
# print('maths' in set_1) it will test  memebership in more efficient way
set_2 ={'history', 'english','cloud computing', 'neural'}
# print(set_1.intersection()) by default it will show same set
# print(set_1.intersection(set_2)) if we pass another set as a parameter it will perform function on it
# print(set_1.union(set_2))
# print(set_1.difference(set_2))


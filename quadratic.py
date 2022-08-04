def func_quad(lst):

    #The function takes in a list of values
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)
    #Print pairs for every item in list

#Function call
func_quad([1,2,3,4,5,6,7,8,9,10])
#We perform n^2 operations for a list of n values
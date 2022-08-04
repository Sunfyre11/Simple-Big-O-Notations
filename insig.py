def comp(lst):

    #Showcasing the dropping of insignificant terms 

    print(lst[0]) # O(1)

    midpoint = int(len(lst) / 2) # O(1/2 * n)
    for value in lst[:midpoint]:
        print(value)
    
    for x in range(10): # O(10)
        print("Hello World")

    # Order of the function is O(1 + n/2 + 10)
    # As n grows larger, the constant terms become insignificant
    # Thus the simplified order is O(n)

# Function call
comp([1,2,3,4,5,6,7,8,9,10])
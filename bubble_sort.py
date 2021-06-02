def bubble_sort(list1):  
      
    for i in range(0,len(list1)-1):  # traverse through all elements
        for j in range(len(list1)-1):  # traverse through the array 
            if(list1[j]>list1[j+1]):   # check if left_pos element > right_pos element
                temp = list1[j]        # if true then swap them   
                list1[j] = list1[j+1]  
                list1[j+1] = temp  
    return list1  
  
list1 = [5, 3, 8, 6, 7, 2]  
print("The unsorted list is: ", list1)  
print("The sorted list is: ", bubble_sort(list1))  

# 1st iteration(list1): 
# [5, 3, 8, 6, 7, 2]
# 5>3 : [3, 5, 8, 6, 7, 2]
# 5<8 : [3, 5, 8, 6, 7, 2]
# 8>6 : [3, 5, 6, 8, 7, 2]
# 8>7 : [3, 5, 6, 7, 8, 2]
# 8>2 : [3, 5, 6, 7, 2, 8]
# 2nd iteration (len(list1)-1):
# [3, 5, 6, 7, 2, 8]
# 3<5 : [3, 5, 6, 7, 2, 8]
# 5<6 : [3, 5, 6, 7, 2, 8]
# 6<7 : [3, 5, 6, 7, 2, 8]
# 7>2 : [3, 5, 6, 2, 7, 8]
# 7<8 : [3, 5, 6, 2, 7, 8]
# .....

# (n - 1) comparisons for n elements each so O(n(n-1)) = O(n(n)) = O(n^2)
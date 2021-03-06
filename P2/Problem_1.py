'''Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))'''



def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    #Returning the number when it is less or equal to 1
    if number <= 1:
    	return number

    my_divsor = 2
    my_result = 0 #setting result to 0

    while my_divsor != my_result:  #If my divisor is not equal to result
    	my_result = number // my_divsor
    	if my_divsor == my_result:
    		return my_result  #printing the result
    	my_divsor += 1 #Incrementing divisor



print ("Pass" if  (2 == sqrt(4)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")

#Edge case
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")

#normal cases
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (6 == sqrt(38)) else "Fail")
print ("Pass" if  (9 == sqrt(81)) else "Fail")
print ("Pass" if  (12 == sqrt(150)) else "Fail")

# Testing for the large number
print("Pass" if (9999 == sqrt(99999999)) else "Fail")

# =============================================================================
# ROUND B EXERCISE 2 - Palindromic Factors
# Google Kickstart 2022
#
# Programming language: Python
#
# Thursday 08/25/2022 
#
# Name: Anh Duc Nguyen 
# Age: 16
# =============================================================================

def solve(n): 
    ans = 0 # create an answer variable
    ar=[] # create an array 
    
    # loop throught all numbers, where i*i is less than the initial number
    # check if they are factors of number, then append them to the array.
    # append also the n/i factor
    i=1 
    while i*i<=n:
        if n%i==0 and i not in ar:
            ar.append(i)
            if i*i<n:
                ar.append(int(n/i))
        i+=1
    # looping through all the factors of n
    for j in ar:
        # change the factor into string
        x = str(j)
        # check if x (string of the factor) is a palindrome number
        c=1 # create a boolean value (now it's True)
        for k in range(int(len(x)/2)):
            if x[k]==x[len(x)-k-1]:
                c=1 # if all the elements are equal, c should in the end
                    # equal to 1
            else:
                c=0 # if there's one pair of elements not equal
                    # to each other, automatically break the for loop
                    # and c will have a value of 0
                break
        # remember that bool(0) is False and 
        # bool("any other integers besides 0") is True
        if bool(c): # check if c is 1, if it is true, we add to our answer
            ans+=1
    
    return ans

#this is the output format that kickstart requires us to print out. 
T = int(input())
for i in range(1,T+1):
    n = int(input())
    print("Case #{}: {}".format(i,solve(n)))

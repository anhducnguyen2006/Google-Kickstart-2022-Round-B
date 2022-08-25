# =============================================================================
# ROUND B EXERCISE 1 - Infinity Area
# Google Kickstart 2022
#
# Programming language: Python
#
# Thursday 08/25/2022 
#
# Name: Anh Duc Nguyen
# Age: 16
# =============================================================================



# define the "pi" number
pi = 3.14159265359

def solve(r,a,b): 
    # first circle on the right has pi*(r**2), we add it beforehand
    # because it's an exception (since when the side is left, the radius
    # has to be devided by b, but the first radius is not devided by b)
    ans=pi*(r**2)
    # side - to check if it's on the right(True) or on the left(False)
    # so we know when to multiply r by a (when it's on the right)
    # or when to devide r by b (when it's on the left)
    side = True
    # we're going to repeat this loop until r = 0, according to the exercise
    while r!=0:
        # check if side is right(True) or left(False),
        # since we started on the left with "pi times r squared", 
        # we have to move to the right, that's why right is decided
        # to be the "True" value and left - the "False" value.
        if side:
            # if it's the right side, we multiply the radius r by a
            r*=a
            # and add to the answer the area of that circle 
            ans+=pi*(r**2)
            # we change the sides to left, since we're done with the right
            # side (we set the left side as "False")
            side=False
        else:
            # the same, but here we have to devide r by b, 
            # remember that we have to use //, not / because,
            # like in the example below the exercise,
            # if we divide 3/6, it has to return 0, not 1/2
            r//=b
            # adding the area of that current circle
            ans+=pi*(r**2)
            # change to the right side (True)
            side=True
    # since y will be considered correct if it is within 
    # an absolute or relative error of 10−6 of the correct answer,
    # we can just round our number to the 6th decimal place.
    return "{:.6f}".format(ans)

# this is the output format that kickstart requires us to print out. 
T = int(input())
for i in range(1,T+1):
    R,A,B = map(int,input().split())
    print("Case #{}: {}".format(i,solve(R,A,B)))

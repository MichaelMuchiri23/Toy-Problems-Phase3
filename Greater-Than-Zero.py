def check_integer(a, b, c):
    #Checking whether the arguments have exactly 2 positive integers.
    if (a > 0 and b > 0 and c <= 0) or (a > 0 and b <= 0 and c > 0) or (a <= 0 and b > 0 and c > 0):
        return True
    else:
        return False

#Case examples to test the function
print(check_integer(1, -1, 0))
print(check_integer(-1, 6, 100))
print(check_integer(1, 1, 1))
print(check_integer(-1, 0, -3))
print(check_integer(1, 10, -2))      
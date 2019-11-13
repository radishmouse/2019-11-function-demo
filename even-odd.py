
# Accept a number as argument
def is_even(number):
    return (number % 2) == 0
    # decide if the number is even
    # if (number % 2) == 0: 
    #     return True
    #     # return True if it's even
    # else:
    #     return False
    #     # return False if it's not even

# print(is_even(5))
# print(is_even(6))

def is_odd(number):
    # return not is_even(number)
    if is_even(number):
        return False
    else:
        return True

print(is_odd(11))

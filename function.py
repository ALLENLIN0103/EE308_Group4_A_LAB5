import random

def szys(f,n1,n2):
    sym = ['＋', '－', '×', '÷']#Defining an array of quadratic operations
    result = 0

    if f == 0:  # addition
        result = n1 + n2

    elif f == 1:  # subtraction
        result = n1 - n2
        result = round((n1 - n2), 2)
    elif f == 2:  # multiplication
        result = n1 * n2
        result = round((n1 * n2), 2)
    elif f == 3:  # division
            # Use the round function to retain one decimal place

            n1 = round(n1,2)

            n2 = round(n2,2)
            result = round((n1 / n2),2)
    return result
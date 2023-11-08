
## this is the "app/my_mod.py file..."

# Here is a normal version of the function

#def enlarge(n):
 #   return n * 100

def enlarge(n):
    """ This is a docstring.
    docstring = documentation inside of a string
    This funciton enlarges a number.
    Pass in n as a parameter.
    Returns a larger version of the number
    """
    return float(n) * 100

## main conditional removes code from global scope to allow clean imports
if __name__ == "__main__":
    

    x = input("please input a number ")
    result = enlarge(x)
    print(result)
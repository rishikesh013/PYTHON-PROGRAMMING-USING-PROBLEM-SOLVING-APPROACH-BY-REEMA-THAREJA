# 5.33 Write a function called printstatus that is passed status code 's', 'm' 'd', 'u' and return the string
# separate married divorced or unmarried respectively. also document the function

def print_status(parm):
    """Function which returns the status of life"""
    if parm.upper() == "M":
        return "Married"
    elif parm.upper() == "S":
        return "Separated"
    elif parm.upper() == "D":
        return "Divorced"
    elif parm.upper() == "U":
        return "Unmarried"
    else:
        return "Please enter the correct choice"


print(print_status("s"))

# Write a function that accepts three integers and returns true if any one is zero


def int_check(a: int, b: int, c: int) -> bool:
    if a == 0 or b == 0 or c == 0:
        return True

    return False


print(int_check(12, 34, 5))
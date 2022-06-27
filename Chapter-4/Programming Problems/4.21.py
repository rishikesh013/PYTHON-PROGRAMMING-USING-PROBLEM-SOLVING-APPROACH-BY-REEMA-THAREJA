# 4.21 Write a program to check if a number is power of 2

def power_of_2(no: int) -> bool:
    if no == 0:
        return False
    while no != 1:
        if no % 2 != 0:
            return False
        no = no // 2

    return True


user_no = int(input("Enter the number to check: "))
if power_of_2(user_no):
    print("It is power of 2")
else:
    print("It is not a power of 2")

# print(power_of_2(user_no))


def is_power_of(num):
    if num != 0 and (num & (num - 1) == 0):
        # a = num & (num - 1)
        # print(a)
        print(f"{user_no: b}")

        return True
    else:
        # a = num & (num - 1)
        # print(a)
        return False


print(f"{user_no: o}")
# print(is_power_of(user_no))

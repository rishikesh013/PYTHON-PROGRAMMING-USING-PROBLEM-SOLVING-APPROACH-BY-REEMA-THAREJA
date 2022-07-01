# 5.36 Write a function that accepts two positive numbers n and m where m<=n, returns number between 1 and n that are
# divisible by m

def check_number(n, m):
    result_numbers = []
    for i in range(1, n + 1):
        if i % m == 0:
            result_numbers.append(i)

    return result_numbers


given_num = check_number(200, 5)
print(given_num)


def greet(parm):
    return f"Hello {parm}"


print(greet('Abi'))

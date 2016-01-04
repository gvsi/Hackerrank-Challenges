input_arr = ["2", "1", "7"]
def input():
    return input_arr.pop(0)

t = int(input())

n = int(input())

def comb(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        return comb(n-1) * 2 - 1

print(comb(6))

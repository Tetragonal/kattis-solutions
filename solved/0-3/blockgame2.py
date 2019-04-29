# a < b
def ans(a, b):
    if a is 1:
        return True
    elif b < 2*a:
        return not ans(b % a, a)
    else:
        return True

a, b = [int(x) for x in input().split()]

if a == b:
    print('win')
else:
    if a > b:
        a,b = b,a
    if ans(a,b):
        print("win")
    else:
        print("lose")

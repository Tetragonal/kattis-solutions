inp = input()
inp = ''.join(['' if idx < len(inp)-1 and inp[idx+1] == x else x for idx, x in enumerate(inp)])
print(inp)
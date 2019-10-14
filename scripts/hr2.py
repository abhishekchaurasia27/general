size = 5
s = 'abcdefghijklmnopqrstuvwxyz'
l = size + (size-1)*2 + (size-2)
loop = size*2 - 1
flag = 0
for i in range(loop):
    if size > 0 and flag == 0:
        #z = s[size-1:i+1:-1]
        print(s[size-1].center(l, '-'))
        size -= 1
    else:
        flag = 1
        size += 1
        print(s[size].center(l, '-'))
        #size += 1
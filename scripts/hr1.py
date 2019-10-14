number = 17
n = len(bin(number)[2:])
for i in range(1,number+1):
    idec = str(i).rjust(n)
    ioct = oct(i)[2:].rjust(n)
    ihex = hex(i).upper()[2:].rjust(n)
    ibin = bin(i)[2:].rjust(n)
    #print(ibin.center(n))
    print("{} {} {} {}".format(idec, ioct, ihex, ibin))
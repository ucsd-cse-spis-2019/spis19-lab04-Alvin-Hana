def recProduct(a,b):
    if b >= 0:
        if b == 1:
            return a
        else:
            return recProduct(a, b-1) + a
    else:
        if b == -1:
            return -a
        else:
            return recProduct(a,b+1) - a
print (recProduct(8,-4))

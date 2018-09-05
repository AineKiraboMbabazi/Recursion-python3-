def power(n,p):
    if p>=1:
        return n*power(n,p-1)

    elif p==0:
        return 1
    
    else:
        p*=-1
        return 1/(n*power(n,p-1))

if __name__ == '__main__':
    print(power(5,-6))

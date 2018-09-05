def power(n,p):
    if not ((isinstance(n,int) and isinstance(p,int) ) or (isinstance(n,float) and isinstance(p,float)) or (isinstance(n,float) and isinstance(p,int) ) or (isinstance(n,int) and isinstance(p,float)) ):
        return 'invalid input'
    if p>=1:
        return n*power(n,p-1)

    elif p==0:
        return 1
    
    else:
        p=abs(p)
        return 1/(n*power(n,p-1))

if __name__ == '__main__':
    print(power(-5,-5))

def compute_sum(list1):
    mysum=0
    for i in list1:
        if isinstance(i,int):
            mysum+=i

        elif isinstance(i,list):
            mysum+=compute_sum(i)

        else:
            pass
    return mysum

if __name__ == '__main__':
    print(compute_sum([1,2,3]))
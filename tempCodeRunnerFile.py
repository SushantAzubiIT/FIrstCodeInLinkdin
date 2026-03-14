def tosortAsscendingorder(*l):
    n=len(l)
    sort=list(l)
    for i in range(n):
        for j in range(n):
            if sort[j]>sort[i]:
                tem=sort[i]
                sort[i]=sort[j]
                sort[j]=tem
            else:
                pass
    
tosortAsscendingorder(1,3,35,3,2342)
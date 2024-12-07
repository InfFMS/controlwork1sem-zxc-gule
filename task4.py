for x in range(2021):
    t=3**100-x
    a=0
    while t!=0:
        if t%3==0:
            a+=1
        t=t//3
    if a==2:
        print(x)
        break
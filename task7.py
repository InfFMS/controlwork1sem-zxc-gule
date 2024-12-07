for i in range(10000, 1000, -1):
    s=str(i)
    a=int(s[0])+int(s[1])
    b=int(s[1])+int(s[2])
    c=int(s[2])+int(s[3])
    n=str(a+b+c-max(a, b, c)-min(a, b, c))
    m=str(max(a, b, c))
    s=n+m
    if s=='1418':
        print(i)
        break
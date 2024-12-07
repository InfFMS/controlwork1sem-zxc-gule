x=125**5+25**9-30
s=''
while x!=0:
    s+=str(x%5)
    x//=5
s=s[::-1]
print(s.count("4"))
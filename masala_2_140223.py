a = list(map(int, input().split()))
max_m,c,b = abs(a[1]-a[0]),a[0],a[1]
dic = {}
for i in range(1,len(a)-1):
    if max_m<abs(a[i]-a[i+1]):
        max_m = abs(a[i]-a[i+1])
        c, b= a[i],a[i+1]
dic.update({max_m:[c,b]})
for i in range(1,len(a)-1):
    if max_m==abs(a[i]-a[i+1]):
        c, b= a[i],a[i+1]
        dic.update({i:[c,b]})
for i in dic:
    print(f"{max_m}({dic[i][0]} va {dic[i][1]})")

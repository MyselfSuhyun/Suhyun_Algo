n,w,h,l = map(int,input().split())
result = (w//l) * (h//l)
print(min(n,result))
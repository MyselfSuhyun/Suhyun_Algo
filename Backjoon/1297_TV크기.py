D, H, W = map(int,input().split())

h = int((H*D)/(((H**2)+(W**2))**(1/2)))
w = int((W*D)/(((H**2)+(W**2))**(1/2)))

print(h,w)
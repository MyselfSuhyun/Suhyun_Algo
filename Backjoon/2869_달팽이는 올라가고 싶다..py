def snail(day, night, height):
    k1 = (height-day)//(day-night)
    while height>k1*(day-night):
        if(height<=k1*(day-night)+day):
            return k1+1
        else:
            k1+=1


A,B,Y = map(int,input().split())
print(snail(A,B,Y))
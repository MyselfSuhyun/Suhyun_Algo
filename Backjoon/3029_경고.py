bh, bm, bs = map(int,input().split(":"))
fh, fm, fs = map(int,input().split(":"))

before = bh*3600 + bm*60 + bs
future = fh*3600 + fm*60 + fs

tmp = future-before
if tmp==-86400:
    print('24:00:00')
else:
    if tmp<=0:
        tmp += 24*3600

    result = ''
    if len(str(tmp//3600))<2:
        result += '0'
    result+=str(tmp//3600)+':'
        if len(str(tmp%3600//60))<2:
            result += '0'
    result += str(tmp%3600//60)+':'
    if len(str(tmp%60))<2:
        result +='0'
    result += str(tmp%60)

    print(result)
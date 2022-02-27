N = float(input())
result = 25.0 + N*0.01
if result <=100:
    print('100.00')
elif result >=2000:
    print('2000.00')
else:
    print(result)
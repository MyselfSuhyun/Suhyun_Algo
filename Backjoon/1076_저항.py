R = {
    'black' : 0,
    'brown' : 1,
    'red' : 2,
    'orange' : 3,
    'yellow' : 4,
    'green' : 5,
    'blue':6,
    'violet' :7,
    'grey': 8,
    'white' : 9,
}

a = R[input()]
b = R[input()]
c = R[input()]
print((a*10+b)*10**c)

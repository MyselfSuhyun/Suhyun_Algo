# 6778. Which Alien?

antenna = int(input())
eyes = int(input())

# Troy Martian
if 3<=antenna and eyes<=4:
    print('TroyMartian')
if antenna<=6 and 2<=eyes:
    print('VladSaturnian')
if antenna<=2 and eyes<=3:
    print('GraemeMercurian')
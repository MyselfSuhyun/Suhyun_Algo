class Mom:
    def walk(self):
        print('사뿐사뿐')


class Dad:
    def walk(self):
        print('저벅저벅')


class Daughter(Mom, Dad):
    pass


class Son(Dad, Mom):
    pass


d = Daughter()
s = Son()

d.walk()
s.walk()
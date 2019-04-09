class info:
    def listadd(self):
        list1.append(self)
    def printinfo(self):
        for li in list1:
            print('{} {} {}'.format(li.name, li.phone, li.sex))

list1 = []

while True:
    a = info()
    a.name = input('이름을 입력하세요 : ')
    if a.name == '그만':
        a.printinfo()
        break
    a.phone = input('전화번호를 입력하세요 : ')
    a.sex = input('성별을 입력하세요 : ')
    if a.sex != 'male' and a.sex != 'female' :
        a.sex = 'unknown'
    a.listadd()
    a.printinfo()
file = open('lab2.txt')
kol_strok = sum(1 for line in file)
l = []
file = open('lab2.txt', encoding = 'utf-8')

class Car:
    def __init__(self, marka, zvet, proizv, V, god, P, dvig, fari, dveri, capot, bagaj):
        self.marka = marka
        self.zvet = zvet
        self.proizv = proizv
        self.V = V
        self.god = god
        self.P = P
        self.dvig = dvig
        self.fari = fari
        self.dveri = dveri
        self.capot = capot
        self.bagaj = bagaj

    def izmen():
        kol_avto = len(l)
        vvod = ''
        while vvod != "0":
            print("Введите номер машины, параметры которой хотите изменить. Если не хотите менять, введите 'Стоп'. Всего машин", kol_avto)
            nomer = input()
            if nomer == "Стоп":
                break
            else:
                try:
                    nomer = int(nomer)
                    if nomer>len(l) or nomer<1:
                        print("Такого номера нет")
                    else:
                        print("Введите имя параметра (Марка, Цвет, Производитель, Объем, Год, Мощность).")
                        param = input()
                        if param != "Марка" and param != "Цвет" and param != "Производитель" and param != "Объем" and param != "Год" and param != "Мощность":
                            print("Вводите корректно")
                        else:
                            if param == "Марка":
                                print(l[nomer-1].marka)
                                print("Введите изменение марки")
                                izm = input()
                                l[nomer-1].marka = izm
                                print("Изменено")
                            if param == "Цвет":
                                print("Введите изменение цвета")
                                izm = input()
                                l[nomer-1].zvet = izm
                                print("Изменено")
                            if param == "Производитель":
                                print("Введите изменение производителя")
                                izm = input()
                                l[nomer-1].proizv = izm
                                print("Изменено")
                            if param == "Объем":
                                print("Введите изменение объема")
                                izm = input()
                                l[nomer-1].V = izm
                                print("Изменено")
                            if param == "Год":
                                print("Введите изменение года выпуска")
                                izm = input()
                                l[nomer-1].god = izm
                                print("Изменено")
                            if param == "Мощность":
                                print("Введите изменение мощности")
                                izm = input()
                                l[nomer-1].P = izm
                                print("Изменено")
                except:
                    print("Вводите корректно")

class Condition():
    def dvig():
        if l[nomer-1].dvig == "Off":
            l[nomer-1].dvig = "On"
            print("Двигатель включен")
        else:
            l[nomer-1].dvig = "Off"
            l[nomer-1].fari = "Off"
            print("Двигатель выключен")
    def fari():
        if l[nomer-1].dvig == "On":
            if l[nomer-1].fari == "Off":
                l[nomer-1].fari = "On"
                print("Фары включены")
            else:
                l[nomer-1].fari = "Off"
                print("Фары выключены")
        else:
            print("Невозможно, двигатель не включен")
    def dveri():
        if l[nomer-1].dveri == "Off":
            l[nomer-1].dveri = "On"
            print("Двери открыты")
        else:
            l[nomer-1].dveri = "Off"
            print("Двери закрыты")

class Izmcol:
    def add():
        vvod = ''
        while vvod != "Стоп":
            print("Введите через пробел марку, цвет, производителя, объем двигателя, год выпуска, мощность. На месте несуществующего параметра напишите 'неизвестно'. Если не хотите вводить, напишите 'Стоп'.")
            avto = input().split()
            if avto != []:
                vvod = avto[0]
            if vvod != 'Стоп':
                if len(avto) != 6:
                    print("Вводите корректно")
                else:
                    obj = Car(avto[0], avto[1], avto[2], avto[3], avto[4], avto[5], "Off", "Off", "Off", "Off", "Off")
                    if obj.marka == '' or obj.zvet == '' or obj.proizv == '' or obj.V == '' or obj.god == '' or obj.P == '':
                        print("Вводите корректно")
                    else:
                        l.append(obj)
                        print("Добавлено")
    def delete():
        kol_avto = len(l)
        vvod = ''
        while vvod != "0":
            print("Введите номер машины, которую хотите удалить. Если не хотите удалять, введите 'Стоп'. Всего машин", kol_avto)
            nomer = input()
            if nomer == "Стоп":
                break
            else:
                try:
                    nomer = int(nomer)
                    if nomer <= 0:
                        print("Отсчет начинается с 1")
                    else:
                        l.remove(l[nomer-1])
                        kol_avto = len(l)
                        print("Удалено")
                except:
                    print("Такого номера в списке нет.")

class Visual:
    def save():
        save_file = open('Save_File.txt', 'w', encoding = 'utf-8')
        save_file = open('Save_File.txt', 'a+', encoding = 'utf-8')

        for i in range(len(l)):
            save_file.write(str(i+1))
            save_file.write(') Марка: ')
            save_file.write(l[i].marka)
            save_file.write(' Цвет: ')
            save_file.write(l[i].zvet)
            save_file.write(' Производитель: ')
            save_file.write(l[i].proizv)
            save_file.write(' Объем двигателя: ')
            save_file.write(l[i].V)
            save_file.write(' Год выпуска: ')
            save_file.write(l[i].god)
            save_file.write(' Мощность: ')
            save_file.write(l[i].P)
            save_file.write(' Двигатель: ')
            save_file.write(l[i].dvig)
            save_file.write(' Фары: ')
            save_file.write(l[i].fari)
            save_file.write(' Двери: ')
            save_file.write(l[i].dveri)
            save_file.write(' Капот: ')
            save_file.write(l[i].capot)
            save_file.write(' Багажник: ')
            save_file.write(l[i].bagaj)
            save_file.write('\n')
        import os
        file.close()
        save_file.close()
        os.remove('lab2.txt')
        os.rename('Save_File.txt', 'lab2.txt')
        print("Сохранено")

    def pokaz():
        Visual.save()
        pok = open('lab2.txt', encoding = 'utf-8')
        print(pok.read())
        pok.close()

for i in range(kol_strok):
    stroka = file.readline()
    stroka = stroka.partition(') ')[2]
    stroka = stroka.partition('Марка: ')[2]
    stroka = stroka.replace('Цвет: ', '')
    stroka = stroka.replace('Производитель: ', '')
    stroka = stroka.replace('Объем двигателя: ', '')
    stroka = stroka.replace('Год выпуска: ', '')
    stroka = stroka.replace('Мощность: ', '')
    stroka = stroka.replace('Двигатель: ', '')
    stroka = stroka.replace('Фары: ', '')
    stroka = stroka.replace('Двери: ', '')
    stroka = stroka.replace('Капот: ', '')
    stroka = stroka.replace('Багажник: ', '')
    stroka = stroka[:-1]
    stroka = stroka.split()
    obj = Car(stroka[0], stroka[1], stroka[2], stroka[3], stroka[4], stroka[5], stroka[6], stroka[7], stroka[8], stroka[9], stroka[10])
    l.append(obj)

prog = "run"

while prog != "Закончить":

    print("Введите операцию (Добавить, Изменить параметры, Изменить состояние, Удалить, Показать, Сохранить, Закончить)")
    vvod = input()
    
    if vvod == "Добавить":
        Izmcol.add()
    if vvod == "Изменить параметры":
        Car.izmen()
    if vvod == "Изменить состояние":
        kol_avto = len(l)
        vvod = ''
        while vvod != "0":
            print("Введите номер машины, состояние которой хотите изменить. Если не хотите менять, введите 'Стоп'. Всего машин", kol_avto)
            nomer = input()
            if nomer == "Стоп":
                break
            else:
                try:
                    nomer = int(nomer)
                    if nomer>len(l) or nomer<1:
                        print("Такого номера нет")
                    else:
                        print("Введите, состояние чего вы хотите изменить (Двигатель, Фары, Двери, Капот, Багажник)")
                        sost = input()
                        if sost != "Двигатель" and sost != "Фары" and sost != "Двери" and sost != "Капот" and sost != "Багажник":
                            print("Вводите корректно")
                        else:
                            if sost == "Двигатель":
                                Condition.dvig()
                            if sost == "Фары":
                                Condition.fari()
                            if sost == "Двери":
                                Condition.dveri()
                            if sost == "Капот":
                                Condition.capot()
                            if sost == "Багажник":
                                Condition.bagaj()
                except:
                    print("Вводите корректно")
    if vvod == "Удалить":
        Izmcol.delete()
    if vvod == "Показать":
        Visual.pokaz()
    if vvod == "Сохранить":
        Visual.save()
    if vvod == "Закончить":
        Visual.save()
        break
file = open('lab2.txt')
kol_strok = sum(1 for line in file)
l = []
file = open('lab2.txt', encoding = 'utf-8')

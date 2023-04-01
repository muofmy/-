#Программа работает с двумя файлами: Names.txt и Count.txt. В Names.txt у нас записаны имена пользователей записанных в определенном порядке.Программа принимает на вход имя.
#И начинает искать его в файле Names.Если оно находит его, то программа выводит под каким номером находится пользователь, иначе программа записывает имя в конец файла.
#И выдает ему новый номер.В файле Count.txt хранится информация о количестве пользователей в списке Names, а также количество обращений к файлу и время последнего обращения.
#Формат записи Count.txt:
#           counts of members - 15
#           counts of file accesses - 9
#           last visit time - 




import datetime

now = datetime.datetime.now()

str_vis = 'last visit time - '
str_ych = 'counts of members - '
str_obr = 'counts of file accesses - '

name = input('Введите ваше имя: ')
file0 = open('Names.txt','r')
file1 = open('Count.txt','r')

count_of_members = file1.readline()
count_of_accesses = file1.readline()
count_of_accesses = count_of_accesses[len(str_obr):]
file1.close()
file1 = open('Count.txt','w')
file1.write(count_of_members)
temp = int(count_of_accesses)
temp += 1
file1.write(str_obr+str(temp))
file1.write('\n'+str_vis+now.strftime("%d-%m-%Y %H:%M")+'\n')
file1.close()


count = 1
flag = True
for i in file0:
    if i[-1] == '\n':
        i = i[:-1]
    if i.upper() == name.upper():
        print('Ваш номер - ', count)
        flag = False
        break
    else:
        count += 1
file0.close()


if flag == True:
    print('Вашего имени нет в списке.')
    file0 = open('Names.txt','a')
    file0.write('\n'+name)
    file0.close()
    print('вы были добавлены под номером',count)
    file1 = open('Count.txt','r')
    count_of_members = file1.readline()
    count_of_accesses = file1.readline()
    file1.close()
    file1 = open('Count.txt','w')
    file1.write(str_ych+str(count)+ '\n')
    file1.write(count_of_accesses)
    file1.write('\n'+str_vis+now.strftime("%d-%m-%Y %H:%M")+'\n')
    file1.close()

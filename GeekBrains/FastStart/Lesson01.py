import os
import psutil
import sys
import shutil

name = input("Представьтесь, пожалуйста: ")

print("\nПривет,", name, "\b. Добро пожаловать в мир языка Python!")

answer = ''

while answer != 'N':
    answer = input("\nЖелаете познать мощь языка Python? (Y/N): ").upper()
    if answer == 'Y':
        print("\nЧто желаете сделать?")
        print(" [ 1 ] - Вывести список файлов")
        print(" [ 2 ] - Вывести информацию о системе")
        print(" [ 3 ] - Вывести список процессов")
        print(" [ 4 ] - Скопировать файлы в директории")
        print(" [ 5 ] - Продублировать указанный файл")
        print(" [ 6 ] - Удалить дубликаты в директории")

        choice = int(input("\nВыберите нужный вариант: "))

        if choice == 1:
            print(os.listdir())
        elif choice == 2:
            print("Информация о системе:")
            print("Количество процессов: ", psutil.cpu_count())
            print("Платформа: ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Текущая директория: ", os.getcwd())
            print("Текущий пользователь: ", os.getlogin())
        elif choice == 3:
            print(psutil.pids())
        elif choice == 4:
            print("Дублирование файлов в текущей директории:", os.getcwd())
            fileList = os.listdir()
            i = 0
            while i < len(fileList):
                if os.path.isfile(fileList[i]):
                    newFile = fileList[i] + '.duplicate'
                    shutil.copy(fileList[i], newFile)
                i += 1
        elif choice == 5:
            print("Дублирование указанного файла")
            fileName = input("Укажите имя требуемого файла: ")
            if os.path.isfile(fileName):
                newFile = fileName + ".duplicate"
                shutil.copy(fileName, newFile)
                if os.path.exists(newFile):
                    print("Файл ", newFile, " был успешно создан.")
                else:
                    print("Сбой при копировании файлов.")
        elif choice == 6:
            print("Удаление дубликатов в директории")
            dirName = input("Укажите имя директории: ")
            fileList = os.listdir(dirName)
            for f in fileList:
                fullName = os.path.join(dirName, fileList[i])
                if fullName.endswith(".duplicate"):
                    os.remove(fullName)
        else:
            print(name, "\b, такой опции нет. Попробуйте ещё раз.")
    elif answer == 'N':
        print("\nНа \"НЕТ\" и суда нет!\nВыход из программы.")
    else:
        print("\nНет такой буквы в этом слове. Вращайте барабан!")

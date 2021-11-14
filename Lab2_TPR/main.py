data = []
with open("Data.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
BP_A = data[0][1] * 5
MP_A = data[0][3] * 5
V_A = BP_A * data[0][2] + MP_A * data[0][4] - data[0][0]

BP_B = data[0][6] * 5
MP_B = data[0][8] * 5
V_B = BP_B * data[0][7] + MP_B * data[0][9] - data[0][5]

BP_C_A = data[0][1] * 4
MP_C_A = data[0][3] * 4
V_C_A = BP_C_A * data[0][12] + MP_C_A * data[0][13] - data[0][0]

BP_C_B = data[0][6] * 4
MP_C_B = data[0][8] * 4
V_C_B = BP_C_B * data[0][12] + MP_C_B * data[0][13] - data[0][5]

F = 0  # Закриття проекту з заводом+
x = max(V_C_A, V_C_B)
V_C = x * data[0][10]

res = max(V_A, V_B, V_A, V_C)
print(" Варіант А")
print("____________________________________________________________________________________________")
print("|    M1   |  D1(A)  |  P1(A) |  D2(A)  |  P2(A) |   ВП(А)  |   MП(А)  | Очікувана Вартість |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")
print("| ", data[0][0], " | ", data[0][1], " | ", data[0][2], " | ", data[0][3], " | ", data[0][4], " | ", BP_A, " | ", MP_A," |    ", V_A, "        |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")

print("\n Варіант В")
print("____________________________________________________________________________________________")
print("|    M1   |  D1(В)  |  P1(В) |  D2(В)  |  P2(В) |   ВП(В)  |   MП(В)  | Очікувана Вартість |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")
print("| ", data[0][5], " | ", data[0][6], " | ", data[0][7], " | ", data[0][8], " | ", data[0][9], " |  ", BP_B, " | ", MP_B," |    ", V_B, "         |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")

print("\n Варіант C Для Великого заводу з затримкою 1 рік(С_А)")
print("____________________________________________________________________________________________")
print("|    M1   |  D1(A)  |  P1(C) |  D2(A)  |  P2(C) |  ВП(C-D) |  MП(C-D) | Очікувана Вартість |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")
print("| ", data[0][0], " | ", data[0][1], " | ", data[0][12], " | ", data[0][3], " | ", data[0][13], " |  ", BP_C_A, " | ", MP_C_A," |    ", V_C_A, "         |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")

print("\n Варіант C Для Маленького заводу з затримкою 1 рік(С_B)")
print("____________________________________________________________________________________________")
print("|    M1   |  D1(B)  |  P1(C) |  D2(В)  |  P2(C) |  ВП(C-D) |  MП(C-D) | Очікувана Вартість |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")
print("| ", data[0][5], " | ", data[0][6], " | ", data[0][12], " | ", data[0][8], " | ", data[0][13], " |  ", BP_C_B, " | ", MP_C_B," |    ", V_C_B, "         |")
print("|_________|_________|________|_________|________|__________|__________|____________________|")

print("\n Варіант C загалом з затримкою 1 рік(С)")
print("_________________________________________________________________________________")
print("|  P3(C)  |  P4(С)  |   C_A  |   C_B   |  ВП(C) |   МП(C)  | Очікувана Вартість |")
print("|_________|_________|________|_________|________|__________|____________________|")
print("|  ", data[0][10], "  |  ", data[0][11], "  |", V_C_A, " | ", V_C_B, " | ", x, "|    ", F, "   |      ", V_C,"       |")
print("|_________|_________|________|_________|________|__________|____________________|")

print("_________________________________________________")
print("|       A       |       B       |       C       |")
print("|_______________|_______________|_______________|")
print("|    ", V_A, "   |    ", V_B, "    |    ", V_C, "    |")
print("|_______________|_______________|_______________|")
if res == V_A:
    print("|    Найбільш ефективний варіант рішення - А    |")
    print("|     Побудовою великого заводу без затримки    |")
    print("|_______________________________________________|")

else:
    if res == V_B:
        print("|    Найбільш ефективний варіант рішення - B    |")
        print("|    Побудова маленького заводу без затримки    |")
        print("|_______________________________________________|")

    else:
        if res == V_C:
            if x == V_C_A:
                print("|    Найбільш ефективний варіант рішення - C    |")
                print("|  Побудова великого заводу з затримкою в 1 рік |")
                print("|_______________________________________________|")
            else:
                if x == V_C_B:
                    print("|    Найбільш ефективний варіант рішення - C    |")
                    print("|   Побудова малого заводу з затримкою в 1 рік  |")
                    print("|_______________________________________________|")



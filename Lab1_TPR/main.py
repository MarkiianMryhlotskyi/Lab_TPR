import numpy np

input_i = np.loadtxt("Data.txt", dtype='i', delimiter=' ')
a = 0.7
# Вальде
Val_1 = min(input_i[0][0], input_i[0][1], input_i[0][2])
Val_2 = min(input_i[1][0], input_i[1][1], input_i[1][2])
Val_3 = min(input_i[2][0], input_i[2][1], input_i[2][2])
# Максімум
Max_1 = max(input_i[0][0], input_i[0][1], input_i[0][2])
Max_2 = max(input_i[1][0], input_i[1][1], input_i[1][2])
Max_3 = max(input_i[2][0], input_i[2][1], input_i[2][2])
# Гурвіца
Gyr_1 = a * Max_1 + (1 - a) * Val_1
Gyr_2 = a * Max_2 + (1 - a) * Val_2
Gyr_3 = a * Max_3 + (1 - a) * Val_3
# Лапласа
Lap_1 = (1 / 3) * (sum(input_i[0]))
Lap_2 = (1 / 3) * (sum(input_i[1]))
Lap_3 = (1 / 3) * (sum(input_i[2]))
# Байеса-Лапласа
p1 = 0.55
p2 = 0.3
p3 = 0.15
Ba_Lap_1 = p1 * input_i[0][0] + p2 * input_i[0][1] + p3 * input_i[0][2]
Ba_Lap_2 = p1 * input_i[1][0] + p2 * input_i[1][1] + p3 * input_i[1][2]
Ba_Lap_3 = p1 * input_i[2][0] + p2 * input_i[2][1] + p3 * input_i[2][2]
# Результат
print("____________________________________________________________________________")
print("|Матриця цінностей| Вальда | Максимум | Гурвіца | Лапласа | Байеса-Лапласа |")
print("|-----------------|--------|----------|---------|---------|----------------|")
print("| ", input_i[0], " |  ", Val_1, "  |  ", Max_1, "   |  ", Gyr_1, " | ", '%.2f' % Lap_1, " |     ", Ba_Lap_1,
      "     |")
print("|  ", input_i[1], "   |  ", Val_2, "  |   ", Max_2, "   |  ", Gyr_2, " | ", '%.2f' % Lap_2, " |     ", Ba_Lap_2,
      "     |")
print("|  ", input_i[2], "   |  ", Val_3, "  |   ", Max_3, "   |  ", Gyr_3, " | ", '%.2f' % Lap_3, " |     ", Ba_Lap_3,
      "     |")
print("|_________________|________|__________|_________|_________|________________|")

MAX_Val = max(Val_1, Val_2, Val_3)
MAX_max = max(Max_1, Max_2, Max_3)
MAX_Gyr = max(Gyr_1, Gyr_2, Gyr_3)
MAX_Lap = max(Lap_1, Lap_2, Lap_3)
MAX_Ba_Lap = max(Ba_Lap_1, Ba_Lap_2, Ba_Lap_3)
i = 0
j = 0
k = 0
# Вальде
if MAX_Val == Val_1:
    i = i + 1
else:
    if MAX_Val == Val_2:
        j = j + 1
    else:
        if MAX_Val == Val_3:
            k = k + 1
# Максімум
if MAX_max == Max_1:
    i = i + 1
else:
    if MAX_max == Max_2:
        j = j + 1
    else:
        if MAX_max == Max_3:
            k = k + 1
# Гурвіца
if MAX_Gyr == Gyr_1:
    i = i + 1
else:
    if MAX_Gyr == Gyr_2:
        j = j + 1
    else:
        if MAX_Gyr == Gyr_3:
            k = k + 1
# Лапласа
if MAX_Lap == Lap_1:
    i = i + 1
else:
    if MAX_Lap == Lap_2:
        j = j + 1
    else:
        if MAX_Lap == Lap_3:
            k = k + 1
# Байеса-Лапласа
if MAX_Ba_Lap == Ba_Lap_1:
    i = i + 1
else:
    if MAX_Ba_Lap == Ba_Lap_2:
        j = j + 1
    else:
        if MAX_Ba_Lap == Ba_Lap_3:
            k = k + 1
#Результат
if max(k, i, j) == i:
    print("|                      Перший варіант найефективніший                      |")
    print("|__________________________________________________________________________|")

else:
    if max(k, i, j) == j:
        print("|                      Другий варіант найефективніший                      |")
        print("|__________________________________________________________________________|")

    else:
        if max(k, i, j) == k:
            print("|                      Третій варіант найефективніший                      |")
            print("|__________________________________________________________________________|")






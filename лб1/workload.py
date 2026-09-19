subject1 = input("Введите название первого предмета: ")
t1 = int(input(f"Введите количество занятий по '{subject1}' за неделю: "))
n1 = int(input(f"Введите продолжительность одного занятия по '{subject1}' в минутах: "))
subject2 = input("Введите название второго предмета: ")
t2 = int(input(f"Введите количество занятий по '{subject2}' за неделю: "))
n2 = int(input(f"Введите продолжительность одного занятия по '{subject2}' в минутах: "))
available_hours = float(input("Введите свободное время на неделю в часах: "))
time1_min = t1 * n1
time2_min = t2 * n2
total_min = time1_min + time2_min
total_hours = total_min / 60
remaining_hours = available_hours - total_hours
print("            РАСЧЕТ НАГРУЗКИ")
print(f"{subject1}: {time1_min} минут")
print(f"{subject2}: {time2_min} минут")
print(f"Общая нагрузка: {total_min} минут ({total_hours:.2f} часов)")
print(f"Остаток свободного времени: {remaining_hours:.2f} часов")
print(f"Нагрузка за 4 недели: {total_hours * 4:.2f} часов")


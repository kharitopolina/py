first_room = input("Введите первую аудиторию: ")
second_room = input("Введите вторую аудиторию: ")
print(f"\nИсходные значения: первая = {first_room}, вторая = {second_room}")
temp = first_room
first_room = second_room
second_room = temp
print(f"После обмена: первая = {first_room}, вторая = {second_room}")
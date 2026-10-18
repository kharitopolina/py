line = input('Введите строку:').strip()
if not line:
    filtered = []
    count = 0
    total = 0
    sorted_filtered = []
else:
    numbers = [int(x) for x in line.split()]
    filtered = [x for x in numbers if x % 3 == 0]
    count = len(filtered)
    total = sum(filtered)
    sorted_filtered = sorted(filtered)
print(filtered)
print(count)
print(total)
print(sorted_filtered)

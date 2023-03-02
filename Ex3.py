num_list = []
list_ord = []

i = 0
while i < 5:
    num = int(input(f"Digite o número: "))
    num_list.append(num)
    i += 1

for i in range(5):
    menor_num = min(num_list)
    list_ord.append(menor_num)
    num_list.remove(menor_num)

print(list_ord)

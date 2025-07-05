#1
listt = (input("dodayte chisla do spisky: "))
list1 = listt.split()
sum = 0
iteration = 0
for i in range (0, len(list1)):
    sum += int(list1[i])
    iteration += 1
print(f"suma chisel: {sum}")
print(f"serednye arifmetichne: {sum/iteration}")
#2
count = 0
listt = (input("dodayte chisla do spisky: "))
list2 = listt.split()
counter = (int(input("vvedit chislo dlya obrahunku: ")))
for i in range (0, len(list2)):
    if counter == int(list2[i]):
        count += 1
print(f"ce chislo povtorilos {count} raziv")
#3
listt = (input("vvedit chisla: "))
list3 = listt.split()
count1 = 0
for i in range (0, len(list3)):
    if int(list3[i]) > 0:
        count1 += 1
print(f"dodatnye chislo povtorilos {count} raziv")
#4
listt = (input("vvedit chisla: "))
list4 = listt.split()
for i in range (0, len(list4)):
    if int(list4[i]) %2 == 0 :
        print(f"index{i}")
#5
counttt = 0
listt = (input("vvedit text: "))
list5 = listt.split()
new_list = [i.capitalize() for i in list5]
print(new_list)
countt = 0
for i in range(0, len(listt)):
    if listt[i].isdigit():
        countt += 1
print(f"kilkist cifer: {countt}")
for i in range(0, len(listt)):
    counttt += listt[i].count("!")
print(f"kilkist [!]: {counttt}")
#6(!)
listt = (input("vvedit text: "))
list6 = listt.split()
for i in range(0,len(list6)):
    for j in range(-1,-i, -1):
        if str(list6[i]) == str(list6[j]):
            list6.remove(list6[j])
print(list6)

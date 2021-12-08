def tables2_10(n):
    for a in range(1, 11):
        print(str(n) + "*" + str(a) + " = " + str(n * a))


list_a = [a for a in range(2, 11)]
for a in list_a:
    tables2_10(a)
    print(" ")
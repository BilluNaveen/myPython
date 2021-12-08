def Display_the_table_from_desired_number_to_desired_number(num):
    for a in range(1, 11):
        print(str(num) + "*" + str(a) + " = " + str(num * a))

try:
    starting_number=int(input())
    end_number=int(input())

    for a in range(starting_number,end_number+1):
        Display_the_table_from_desired_number_to_desired_number(a)
        print(" ")
except:
    print("Error")
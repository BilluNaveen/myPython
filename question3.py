def good_name(name, number_of_times):
    for a in range(number_of_times):
        print(name)


if __name__ == "__main__":
    name = input()
    number_of_times = int(input())
    good_name(name, number_of_times)
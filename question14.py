def rightAngeTriangle(n):
    count = n - 1
    for a in range(1, n + 1):
        spaces = "  " * count
        print(spaces + "* " * a)
        count = count - 1



n=int(input())
rightAngeTriangle(n)
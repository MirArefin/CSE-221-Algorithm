for i in range(int(input())):
    n = input()
    n=n.split(' ')
    if n[2] == '+':
       a=(int(n[1]) + int(n[3]) )
    if n[2] == '-':
       a=(int(n[1]) - int(n[3]) )
    if n[2] == '/':
       a=(int(n[1]) / int(n[3]) )
    if n[2] == '*':
       a=(int(n[1]) * int(n[3]) )
    print("{:.6f}".format(a))

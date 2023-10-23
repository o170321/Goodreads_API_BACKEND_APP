# cook your dish here
n = int(input())
p = ["a", "e", "i", "o", "u"]
for i in range(n):
    str2 = ""
    po = int(input())
    k = 0
    str1 = input()
    for i in str1:
        if i not in p:
            k = k+1
            if k == 4:
                print("NO")
                break
        else:
            if i in p:
                k = 0
    if k < 4:

        print("YES")

from time import sleep
a = [111,922,115,116,72,131,8,12,12,1,2,33,44,5566,778,4,434,32,11111,323,1,89,0,3,0.10,-1]
b = len(a)
while 1==1:
    for i in range(0,(b-1)):
        if a[i] > a[i+1]:
            a[i+1],a[i] = a[i],a[i+1]
            print(a)  # while与if条件只有while成立，if不成立时才会持续循环






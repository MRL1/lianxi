#使用 for 循环和 range 实现输出  1 - 2  +  3  -­ 4  +  5  -­ 6  ...  +  99  的和
total_01=0
total_02=0
for i in range(1,100):
    if i%2==1:
        i+=2
        total_01+=i
    else:
        i+=2
        total_02+=-i
print(total_01+total_02)
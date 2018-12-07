# 使用 while 循环实现输出 2 ‐  3  +  4  ‐  5  +  6  ...  +  100  的和
i=2
j=3
total_01=0
total_02=0
while i<=100:
    if i%2 == 0:
        i+=2
        total_01=total_01+i
while j<=100:
    if j % 2 == 1:
        j+=2
        total_02=total_02+j
print(total_01-total_02)

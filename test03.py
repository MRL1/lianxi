# 使用 while 循环实现输出  1，2，3，4，5，   7，8，9，    11，12
i=0
while i<12:
    i += 1
    if i<=5:
        print(i)
    if i>6 and i<10:
        print(i)
    if i>=11 and i<=12:
        print(i)
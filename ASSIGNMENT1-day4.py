for num in range(1042000,702648265):
    sum = 0
    temp=num
    while temp>0:
        digit=temp%10
        sum=(digit*digit*digit)+sum
        temp//=10
    if num == sum:
            print("The first Armstrong number is:",sum)

    
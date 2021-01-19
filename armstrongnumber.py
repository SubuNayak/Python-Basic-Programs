def armstrong(n):
    temp = n
    scd = 0
    order =len(str(n))
    while (temp > 0):
        ld = temp % 10
        temp //= 10
        scd += ld ** order
    if n == 0:
        return True

    if scd == n :
        return  True
    else:
        return False


num = int ( input ( "Input :"))
if armstrong(num):
    print(num, ' is an armstrong number')
else:
    print(num,'is not an armstrong number')
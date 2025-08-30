# Program to convert a decimal (base 10) number to binary (base 2)
num = int(input("Enter a integer(base 10) number :"))
int_num = num
binary = ""

if num == 0 :
    binary = "0"
else :
    while num > 0 :
        r = num % 2
        binary = str(r) + binary
        num = num  // 2
print(f'The binary(base 2) number of {int_num} is {binary}')


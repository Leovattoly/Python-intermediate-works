def digitSum(number):
    if number==0:
        return 0;
    d = number % 10
    number = number// 10
    return(d+ digitSum(number))

print(digitSum(135789))
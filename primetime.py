import math
starting_num = 2
finishing_num = 100
i = starting_num

#add a new comment
while i <= finishing_num:
    j = 2
    prime_flag = True
    while j <= math.sqrt(i):
        if i % j == 0:
            prime_flag = False           
        j += 1
    if prime_flag == True:
        print(i, "is a prime number")
    i += 1
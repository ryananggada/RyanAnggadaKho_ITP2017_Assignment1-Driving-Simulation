def module_by_42(number):     #function to module the inputted number by 42
    remainder = number % 42
    return remainder

distinct_number = []     #the array for distinct numbers

for i in range(10):     #loop to find the distinct numbers
    input_num = int(input("Enter number: "))
    module = module_by_42(input_num)
    if module not in distinct_number:
        distinct_number.append(module)

print(len(distinct_number))     #output the number of distinct numbers

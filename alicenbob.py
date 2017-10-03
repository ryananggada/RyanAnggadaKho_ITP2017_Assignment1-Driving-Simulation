def minus_two(number):     #function to take 2 stones away
    number -= 2
    return number

rock_number = int(input("Enter number of rocks: "))     #input the number of rocks

while rock_number > 1:     #loop to take 2 stones until the stone left is either 1 or 0
    rock_number = minus_two(rock_number)

if rock_number == 1:     #condition whether Alice or Bob wins (Alice wins if stone left is 1, otherwise Bob wins)
    print("Alice wins!")
else:
    print("Bob wins!")

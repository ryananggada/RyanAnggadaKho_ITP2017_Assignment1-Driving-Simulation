def swap_cup(first_cup, second_cup):     #the function to swap the cup position
    temp = second_cup
    second_cup = first_cup
    first_cup = temp
    return first_cup

initial_position = 1     #this is the initial position of the ball, which is at left
moves = input("Enter turns in capital alphabet: ")     #input the moves of the cups

for i in range(len(moves)):     #loop to determine the position of the ball by calling functions until the number of moves are gone
    if moves[i] == "A":
        ball_position = swap_cup(1, 2)
    elif moves[i] == "B":
        ball_position = swap_cup(2, 3)
    elif moves[i] == "C":
        ball_position = swap_cup(1, 3)

print("The ball is in position {}.".format(ball_position))     #outputs the position of the ball

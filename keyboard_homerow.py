row1 = "QqWwEeRrTtYyUIiOoPp"
row2 = "AaSsDdFfGgHhJjKkLl"
row3 = "ZzXxCcVvBbNnMm"

print("Give me a string so that I can check if all the characters in that string is on the same row of the keyboard")
usr_input = input()

match_counter_Row1 = 0
match_counter_Row2 = 0
match_counter_Row3 = 0

for char in usr_input:
    if char in row1:
        match_counter_Row1 +=1

    if char in row2:
        match_counter_Row2 +=1

    if char in row3:
        match_counter_Row3 +=1

if ((match_counter_Row1 == len(usr_input)) or (match_counter_Row2 == len(usr_input)) or (match_counter_Row3 == len(usr_input))):
    print("The string " + usr_input + " can be typed on the same row of the keyboard")
else:
    print("The string cannot be typed on the same row of the keyboard")

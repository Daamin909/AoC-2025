with open("input.txt", "r") as f:
    lines = f.read().splitlines()

position = 50
number_of_zeroes = 0

for line in lines:
    number = int(line[1:])
    if line[0] == "L":
        position = (position - number) % 100
        if position == 0:
            number_of_zeroes += 1

    else: 
        position = (position + number) % 100
        if position == 0:
            number_of_zeroes += 1

print(number_of_zeroes)

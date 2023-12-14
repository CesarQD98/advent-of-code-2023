MAX_REDS = 12
MAX_GREENS = 13
MAX_BLUES = 14

sum = 0

with open("./data/02-puzzle-input.txt", "r") as file:
    for line in file:
        reds = []
        blues = []
        greens = []

        first_space_index = line.find(" ")
        semicolon_index = line.find(":")
        game_id = int(line[first_space_index + 1 : semicolon_index])

        temp = line[semicolon_index + 2 : -1].split("; ")
        sets = [elem.split(", ") for elem in temp]

        for elem in sets:
            for ball_count in elem:
                if ball_count.endswith("red"):
                    reds.append(int(ball_count[:-3]))
                if ball_count.endswith("blue"):
                    blues.append(int(ball_count[:-4]))
                if ball_count.endswith("green"):
                    greens.append(int(ball_count[:-5]))

        valid_reds = all(elem <= MAX_REDS for elem in reds)
        valid_blues = all(elem <= MAX_BLUES for elem in blues)
        valid_greens = all(elem <= MAX_GREENS for elem in greens)

        if valid_reds and valid_blues and valid_greens:
            sum += game_id

print("sum → ", sum)

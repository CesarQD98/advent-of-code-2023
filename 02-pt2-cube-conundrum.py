sum = 0

with open("./data/02-puzzle-input.txt", "r") as file:
    for raw_line in file:
        reds = []
        blues = []
        greens = []

        line = raw_line.replace("\n", "")

        first_space_index = line.find(" ")
        semicolon_index = line.find(":")
        game_id = int(line[first_space_index + 1 : semicolon_index])

        temp = line[semicolon_index + 2 :].split("; ")
        sets = [elem.split(", ") for elem in temp]

        for elem in sets:
            for ball_count in elem:
                if ball_count.endswith("red"):
                    reds.append(int(ball_count[:-3]))
                if ball_count.endswith("blue"):
                    blues.append(int(ball_count[:-4]))
                if ball_count.endswith("green"):
                    greens.append(int(ball_count[:-5]))

        max_red = max(reds)
        max_blue = max(blues)
        max_green = max(greens)

        sum += max_red * max_blue * max_green

print("sum → ", sum)

output = []
sum = 0

with open("/data/01-puzzle-input.txt", "r") as file:
    for line in file:
        temp = []
        for ch in line:
            if ch.isdigit():
                temp.append(ch)
        output.append(temp)

for item in output:
    sum += int(item[0] + item[-1])

print(sum)

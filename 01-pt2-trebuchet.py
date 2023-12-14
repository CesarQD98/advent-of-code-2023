def positions(string, substring):
    pos = []
    if substring in string:
        for i, l in enumerate(string):
            if l == substring[0]:
                if string[i : i + len(substring)] == substring:
                    pos.append(i)
    return pos


digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

output = []
sum = 0

with open("./data/01-puzzle-input.txt", "r") as file:
    for line in file:
        numbers = []
        for key, value in digits.items():
            if key in line:
                pos = positions(line, key)
                for p in pos:
                    numbers.append((p, value))

        for index, ch in enumerate(line):
            if ch.isdigit():
                numbers.append((index, int(ch)))
        output.append(numbers)

print(output)

for index, item in enumerate(output):
    sum += min(item)[1] * 10 + max(item)[1]

print(sum)

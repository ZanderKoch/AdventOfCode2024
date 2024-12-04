"""
Pair up the numbers and measure how far apart they are. Pair up the smallest
number in the left list with the smallest number in the right list, then the
second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to
add up all of those distances. For example, if you pair up a 3 from the left
list with a 7 from the right list, the distance apart is 4; if you pair up a 9
with a 3, the distance apart is 6.

To find the total distance between the left list and the right list, add up the
distances between all of the pairs you found.
"""

leftIds = []
rightIds = []

with open("1/input.txt", "r") as file:

    for line in file:
        lineIds = line.strip().split("   ")
        leftIds.append(int(lineIds[0]))
        rightIds.append(int(lineIds[1]))

# print(leftIds[0:3])
# print(rightIds[0:3])

leftIds.sort()
rightIds.sort()

print(leftIds[0:3])
print(rightIds[0:3])

total = 0
for i in range(0, len(leftIds)):
    total += abs(leftIds[i] - rightIds[i])

print(f"total: {total}")


"""
part two:
This time, you'll need to figure out exactly how often each number from the
left list appears in the right list. Calculate a total similarity score by
adding up each number in the left list after multiplying it by the number of
times that number appears in the right list.
"""

similarity = 0
for i in range(0, len(leftIds)):
    similarity += leftIds[i] * rightIds.count(leftIds[i])

print(f"similarity: {similarity}")

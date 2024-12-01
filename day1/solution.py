from collections import Counter

file_name = "day1\input.txt"

with open(file_name, "r") as file:
    data = file.readlines()

left_list = []
right_list = []

for line in data:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

print("Total distance:", total_distance)

right_count = Counter(right_list)

similarity_score = sum(num * right_count[num] for num in left_list)
print("Similarity score:", similarity_score)
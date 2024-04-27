from collections import defaultdict

# Read input
flat_num = int(input())
flats = list(input().strip())
types = set(flats)

shortest_interval = float('inf')
curr_pokemon = defaultdict(int)
closest_left = 0

for right in range(flat_num):
    curr_pokemon[flats[right]] += 1

    while (closest_left + 1 <= right and
           flats[closest_left] in curr_pokemon and
           curr_pokemon[flats[closest_left]] > 1):
        curr_pokemon[flats[closest_left]] -= 1
        closest_left += 1

    if len(curr_pokemon) == len(types):
        shortest_interval = min(shortest_interval, right - closest_left + 1)

print(shortest_interval)
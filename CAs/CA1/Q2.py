s1 = input()
s2 = input()
# sorted_s1 = ''.join(sorted(s1))
# sorted_s2 = ''.join(sorted(s2))
odd_part1 = s1[1::2]  # Characters at odd indices
even_part1 = s1[::2]  # Characters at even indices
odd_part2 = s2[1::2]  # Characters at odd indices
even_part2 = s2[::2]  # Characters at even indices
sorted_odd_part1 = ''.join(sorted(odd_part1))
sorted_odd_part2 = ''.join(sorted(odd_part2))
sorted_even_part1 = ''.join(sorted(even_part1))
sorted_even_part2 = ''.join(sorted(even_part2))

if sorted_odd_part1 == sorted_odd_part2 and sorted_even_part1 == sorted_even_part2:
    print("yes")
else:
    print('no')
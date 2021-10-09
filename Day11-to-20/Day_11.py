#linear search or sequential search...

nums = list(map(int, input().split()))
target = int(input())

for num in nums:
    if num == target:
       print(f"the number was found at {nums.index(num) + 1}th position.")

# Day 11
#DSA begins

nums = [0, 1, 3, 0, 12]

# new_arr = [num for num in arr if num != 0]
# new_arr.extend([0 for i in range(arr.count(0))])
#
# print(new_arr)

j = 0
for num in nums:
    if num != 0:
        nums[j] = num
        j += 1

for i in range(j, len(nums)):
    nums[i] = 0

print(nums)

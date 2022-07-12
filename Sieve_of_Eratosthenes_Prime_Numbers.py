from math import sqrt

num = int(input('Enter a number: '))
nums = range(2, num+1)
end_num = int(sqrt(nums[-1])) + 1
trial = 0

while nums[trial] < end_num:
    new_nums = [i for i in nums if i==nums[trial] or i%nums[trial]>0]
    nums = new_nums
    trial += 1

print(*nums)
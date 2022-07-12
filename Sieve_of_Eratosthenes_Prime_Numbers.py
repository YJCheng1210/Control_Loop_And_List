num = int(input('Enter a number: '))
nums = range(2, num+1)
trial = 0

while trial < round(len(nums)/2):
    new_nums = [i for i in nums if i==nums[trial] or i%nums[trial]>0]
    nums = new_nums
    trial += 1

print(*nums)

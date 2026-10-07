def counting_sort(nums: list):

    n = max(nums)+1
    output = [0] * len(nums)
    count = [0] * n

    for i in nums:
        count[i]+=1

    # cummualative sum
    for i in range(1,n):
        count[i] += count[i-1]

    i = 0
    for i in nums:
        output[count[i]-1] = i
        count[i] -=1

    return output

nums = [4,2,2,8,3,3,1]
print(counting_sort(nums))


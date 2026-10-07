def countsort(nums,place):
    max_ = max(nums)
    n = len(nums)
    output = [0] *n
    count = [0]* 10

    for i in nums:
        count[i//place %10] +=1
    
    # cummulative sum
    for i in range(1,10):
        count[i] += count[i-1]

    for i in range(n-1,-1,-1):
        output[count[nums[i]//place %10]-1] = nums[i]
        count[nums[i]//place %10] -=1

    for i in range(n):
        nums[i] = output[i]
    

def radix_sort(nums):
    max_ = max(nums)

    place = 1
    while max_//place >0:
        countsort(nums,place)
        print(nums)
        place *= 10
    
    

# data = [121, 432, 564, 23, 1, 45, 788]
# data = [15252,16764,27963,7817,26155,20757,3478,22602,20404,6739,16790,10588,16521,6644,20880,15632,27078,25463,20124,15728,30042,16604,17223,4388,23646,32683,23688,12439,30630,3895,7926,22101,32406,21540,31799,3768,26679,21799,23740]
data = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(data)
print(data)


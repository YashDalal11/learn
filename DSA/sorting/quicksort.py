def quicksort(nums,low,high):
    if high<=low:
        return
    pivot = partitiion(nums,low,high)
    quicksort(nums,low,pivot-1)
    quicksort(nums,pivot+1,high)

def partitiion(nums,low,high):
    i = low
    key = high
    for j in range(i+1,len(nums)):
        if nums[j]>=nums[key]:
            # swap
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp

            i+=1

    # swap
    temp = nums[i] 
    nums[j] = nums[key]
    nums[key] = temp

    return i
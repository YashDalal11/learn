import heapq
def findMaxSum(nums1, nums2, k):
    idx = sorted(range(len(nums1)), key = lambda i: nums1[i])
    nums1_sorted = [nums1[i] for i in idx]
    nums2_sorted = [nums2[i] for i in idx]

    ans = [0] * len(nums1)

    current_sum = 0
    heap =[]
    prev = -1
    for i in idx:
        
        if i>0 and nums1[i]==nums1[prev]:
            ans[i] = ans[prev]
        else:
            ans[i] = current_sum

        heapq.heappush(heap,nums2[i])
        current_sum+= nums2[i]

        if len(heap)>k:
            removed = heapq.heappop(heap)
            current_sum-= removed
        
        prev = i

    return ans

nums1 = [25,15,1,28,3,13,29,26,1,2,28,5,2,14,19,2,4]
nums2 = [25,21,3,23,26,6,30,22,27,21,24,27,15,17,15,16,25]


print(findMaxSum(nums1,nums2,9))
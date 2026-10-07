from sortedcontainers import SortedList

def maxScore(nums1, nums2, k):
    n = len(nums1)
    idx = sorted(range(n), key = lambda i: nums1[i])
    print(idx)
    sum_= 0
    q = SortedList([])
    ans = 0 
    for i in range(len(idx)):
        if i>=k:
            q.remove(nums2[idx[i-k]])
            sum_-=nums1[idx[i-k]]
        q.add(nums2[idx[i]])
        sum_+=nums1[idx[i]]
        if i<k:
            continue
        ans = max(ans, sum_ * q[0])

    return ans

nums1 = [1,3,3,2]
nums2 = [2,1,3,4]
k = 3
maxScore(nums1,nums2,k)
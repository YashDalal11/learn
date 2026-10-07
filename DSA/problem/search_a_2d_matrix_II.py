def searchMatrix(matrix, target): 
    n = len(matrix)
    m = len(matrix[0])

    s,e = 0,n
    while s<e:
        mid = (e+s)//2

        if matrix[mid][-1] >= target:
            e = mid
        else:
            s = mid+1

    row = s

    left,right = 0,m-1
    while left<=right:
        mid = (left+right)//2

        if matrix[s][mid] == target:
            return True
        elif matrix[s][mid] < target:
            left= mid+1
        else:
            right = mid-1
    return False

matrix = [[1,4,7,11,15],[2,5,8,12,20],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

print(searchMatrix(matrix,20))
from collections import defaultdict

def maxTaxiEarnings(n, rides) -> int:
    
    end_point = defaultdict(list)
    rides = sorted(rides,key =lambda ride: ride[1])

    for i in range(len(rides)):
        ride = rides[i]
        end_point[ride[1]].append(i)

    stops = [0] * (n+1)
    for i in range(1,n+1):
        if i not in end_point:
            stops[i] = stops[i-1]
            continue
        
        rides_for_current_stop = end_point[i]
        max_= 0
        for ride_index in rides_for_current_stop:
            ride = rides[ride_index]
            max_ = max(max_, ride[1]-ride[0]+ride[2]+stops[ride[0]])

        stops[i] = max(stops[i-1],max_)

    return stops[n]


rides = [[9,10,2],[4,5,6],[6,8,1],[1,5,5],[4,9,5],[1,6,5],[4,8,3],[4,7,10],[1,9,8],[2,3,5]]
ans= maxTaxiEarnings(10,rides)
print(ans)
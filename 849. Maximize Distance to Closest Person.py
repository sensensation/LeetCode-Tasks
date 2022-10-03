#849. Maximize Distance to Closest Person
# You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to the closest person.

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev=None                              #prev occupied seat counter
        dis=float('-inf')                      #distance starting from negative infinity
        for i in range(len(seats)):            #iterating through seats
            if seats[i]==1:                    #if seat is occupied
                if prev is None:               #if this is the first iteration of loop
                    dis=i                      #distance become 0
                else:
                    dis=max(dis, (i-prev)//2)  #ideal seat alex wants to sit from both ends (in between)
                prev=i                         #increasing the prev counter everytime
        return max(dis, len(seats)-prev-1)
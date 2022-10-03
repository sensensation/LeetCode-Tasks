# 881. Boats to Save People
# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.


def numRescueBoats(people, limit):
    """
    :type people: List[int]
    :type limit: int
    :rtype: int
    """
    boats = 0
    people.sort()
    i, j = 0, len(people) - 1

    while i <= j:
        boats += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return boats


numRescueBoats([3,2,2,1],3)

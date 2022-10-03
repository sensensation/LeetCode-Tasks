#485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.
nums = [1,0,1,1,0,1,1,1,0]
memory = 0
iterator = 0
for i in nums:
    if i == 1:
        iterator += 1

    else:
        if iterator > memory:
            memory = iterator
            iterator = 0
if memory < iterator:
    memory = iterator

print(memory)






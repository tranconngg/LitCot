def findMaxAverage(nums, k):
        if len(nums)==1:
            return nums[0]
        left, right = 0,0
        sum = 0
        max_tb = -99999999999
        while right < len(nums):
                sum+=nums[right]
                if right -left +1 == k:
                        tb = float(sum) / k
                        if tb > max_tb:
                            max_tb=tb
                        sum -= nums[left]
                        left +=1
                right +=1
        return max_tb
print(findMaxAverage([-1,-2,-3,-4,-6,-8],5))
print(findMaxAverage([5,2,6,8,2,4,6,8,4],5))
print(findMaxAverage([-2,-3,5,7,-8],3))
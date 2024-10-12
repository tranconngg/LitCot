def maxOperations(nums, k):
        nums=sorted(nums)
        left=0
        right = len(nums)-1
        cnt =0
        while left <right:
            if nums[left]+nums[right] ==k:
                left +=1
                right -=1
                cnt +=1
            elif nums[left]+nums[right] <k:
                left +=1
            else:
                right -=1
        return cnt


print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],2))
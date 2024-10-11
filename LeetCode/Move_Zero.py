# sol 1
def moveZeroes1(nums):
        cnt = 0
        for i in range(0,len(nums)-2):
            if nums[i] == 0:
                zero = nums.pop(i)
                cnt +=1
        list_zero = [0] * cnt
        return nums + list_zero

print(moveZeroes1([0,1,0,3,12]))

#  sol 2
def moveZeroes2(self, nums):
        right=1
        left=0
        for right in range(0,len(nums)):
            if nums[right] != 0:
                nums[left],nums[right]=nums[right],nums[left]
                left +=1
            
        return nums

print(moveZeroes1([0,1,0,3,12]))
        

def increasingTriplet(nums):
        if len(nums) < 3:
           return False
        # khởi tạo chúng bằng dương vc
        min = float('inf')
        tb = float('inf')
    
        for num in nums:
            if num <= min:
                min = num
            elif num <= tb: 
                min = num
            else:
                return True

        return False
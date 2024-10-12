def maxArea(height):
        left=0
        right = len(height)-1
        dientich, chieucao, chieurong= 0,0,0
        max_dientich=0
        while left < right:
            chieucao  = min(height[left], height[right])
            chieurong = right - left
            dientich = chieucao * chieurong
            if dientich > max_dientich:
                  max_dientich = dientich
            if height[left] < height[right]:
                  left += 1
            else:
                  right -=1
        return max_dientich
print(maxArea([1,8,6,2,5,4,8,3,7]))

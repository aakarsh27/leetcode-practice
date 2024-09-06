def findMin(nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
                
        return nums[left]
    
print(findMin([3,4,5,6,7,1,2]))
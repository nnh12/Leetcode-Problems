class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_vol = 0

        while ( left < right ):
            length = right - left
            width = min(height[left], height[right])
            max_vol = max(length * width, max_vol)

            print(right, left, max_vol)

            if left < right and height[left] < height[right]:
                left += 1
            elif left < right and height[left] > height[right]:
                right -= 1
            elif left < right and height[left] == height[right]:
                if height[left + 1] > height[right - 1]:
                    right -= 1
                else:
                    left += 1
            else:
                break
        
        return max_vol

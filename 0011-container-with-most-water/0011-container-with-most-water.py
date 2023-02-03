class Solution(object):
    def maxArea(self, heights):
        left = 0
        right = len(heights) - 1
        water = 0
        while left < right:
            width = right - left
            height = min(heights[left],heights[right])
            water = max(water,width*height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return water
        
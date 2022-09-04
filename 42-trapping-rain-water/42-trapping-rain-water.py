class Solution:
    def trap(self, heights: List[int]) -> int:
        stack =[]
        totalRain = 0

        for index in range(len(heights)):
            while stack and heights[stack[-1]] < heights[index]:

                height = heights[stack.pop()]
                if len(stack) == 0:
                    break
                distance = index - stack[-1] - 1
                boundHeight = min(heights[stack[-1]],heights[index]) - height
                totalRain += distance * boundHeight
            stack.append(index)

        return totalRain
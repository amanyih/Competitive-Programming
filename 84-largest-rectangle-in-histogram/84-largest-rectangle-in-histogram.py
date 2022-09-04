class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for index in range(len(heights)):
            curIndex = index
            while stack and stack[-1][-1] > heights[index]:
                maxArea = max(maxArea,(index - stack[-1][0]) * stack[-1][-1])
                print(maxArea)
                curIndex = stack.pop()[0]
            stack.append([curIndex,heights[index]])

        while stack:
            maxArea = max(maxArea,(len(heights) - stack[-1][0]) * stack.pop()[-1])

        return maxArea
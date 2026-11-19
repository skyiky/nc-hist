class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest = 0
        for i, height in enumerate(heights):
            curr_rectangle_starting_index = i
            while stack and stack[-1][1] > height:
                candidate = (i - stack[-1][0]) * stack[-1][1] # w x h
                largest = max(largest, candidate) 

                #curr_rectangle_starting_index -= 1
                curr_rectangle_starting_index = stack[-1][0]

                stack.pop()
            stack.append((curr_rectangle_starting_index, height))
        
        for i, height in stack:
            candidate = (len(heights) - i) * height # w x h
            largest = max(largest, candidate) 

        return largest
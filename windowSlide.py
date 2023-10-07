class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        result = []
        max_index = 0
        max_val = float('-inf')
        dq = []  # Use a list to simulate a deque

        for i in range(len(nums)):
            # Remove elements from the left of the deque that are outside the current window
            while dq and dq[0] < i - k + 1:
                dq.pop(0)

            # Remove elements from the right of the deque that are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current element's index to the right of the deque
            dq.append(i)

            # If the current index is at least k - 1, add the maximum element to the result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
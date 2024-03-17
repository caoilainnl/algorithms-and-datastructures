from collections import deque

class SlidingWindowMaximum:
    def max_sliding_window(self, nums, k):
        """
        Finds the maximum in every sliding window of size k in the array nums.
        Uses a deque to maintain indices of useful elements for the current window.
        """
        if not nums or k == 0:
            return []

        n = len(nums)
        result = []
        dq = deque()  # Deque to store indices of useful elements

        for i in range(n):
            # Remove indices that are out of the current window
            while dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements that are smaller than the current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current element's index
            dq.append(i)

            # Append the maximum for the current window to the result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Testing the implementation
def main():
    print("Running exhaustive tests for Sliding Window Maximum...")

    # Test Case 1: Basic test case
    print("\nTest Case 1: Basic test case")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    solution = SlidingWindowMaximum()
    print(f"Max sliding window for {nums} with k={k} (Expected [3, 3, 5, 5, 6, 7]): {solution.max_sliding_window(nums, k)}")

    # Test Case 2: Single element in each window
    print("\nTest Case 2: Single element in each window")
    nums = [4, 2, 12, 5, 8]
    k = 1
    print(f"Max sliding window for {nums} with k={k} (Expected [4, 2, 12, 5, 8]): {solution.max_sliding_window(nums, k)}")

    # Test Case 3: Window size equals array size
    print("\nTest Case 3: Window size equals array size")
    nums = [10, 20, 30, 40]
    k = 4
    print(f"Max sliding window for {nums} with k={k} (Expected [40]): {solution.max_sliding_window(nums, k)}")

    # Test Case 4: All elements are the same
    print("\nTest Case 4: All elements are the same")
    nums = [5, 5, 5, 5, 5]
    k = 3
    print(f"Max sliding window for {nums} with k={k} (Expected [5, 5, 5]): {solution.max_sliding_window(nums, k)}")

    # Test Case 5: Decreasing sequence
    print("\nTest Case 5: Decreasing sequence")
    nums = [9, 8, 7, 6, 5, 4]
    k = 2
    print(f"Max sliding window for {nums} with k={k} (Expected [9, 8, 7, 6, 5]): {solution.max_sliding_window(nums, k)}")

    # Test Case 6: Increasing sequence
    print("\nTest Case 6: Increasing sequence")
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    print(f"Max sliding window for {nums} with k={k} (Expected [3, 4, 5, 6]): {solution.max_sliding_window(nums, k)}")

    # Test Case 7: Array smaller than k
    print("\nTest Case 7: Array smaller than k")
    nums = [1, 2, 3]
    k = 5
    print(f"Max sliding window for {nums} with k={k} (Expected []): {solution.max_sliding_window(nums, k)}")

    # Test Case 8: Empty array
    print("\nTest Case 8: Empty array")
    nums = []
    k = 3
    print(f"Max sliding window for {nums} with k={k} (Expected []): {solution.max_sliding_window(nums, k)}")

    # Test Case 9: Single element array
    print("\nTest Case 9: Single element array")
    nums = [10]
    k = 1
    print(f"Max sliding window for {nums} with k={k} (Expected [10]): {solution.max_sliding_window(nums, k)}")


if __name__ == "__main__":
    main()

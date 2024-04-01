def find_subsets(nums):
    subsets = []

    # Define a recursive helper function to generate subsets
    def backtrack(start, subset):
        # Add the current subset to the list of subsets
        subsets.append(subset[:])
    
        # Iterate through the remaining elements starting from the current index
        for i in range(start, len(nums)):
            # Include the current element in the subset
            subset.append(nums[i])

            # Recursively generate subsets with the current element included
            backtrack(i + 1, subset)

            # Backtrack and remove the current element to explore other subsets
            subset.pop()

    # Start the backtracking process from index 0 with an empty subset
    backtrack(0, [])

    return subsets

# Example usage:
nums = [1, 2, 3]
result = find_subsets(nums)
print("Subsets:", result)
# print(result[1][0])

# 3Sum
# Return all unique triplets [nums[i], nums[j], nums[k]] with distinct indices and sum == 0.
# The solution set must not contain duplicate triplets (same three values).

# Example:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]  (order of triplets / elements in list may vary)

# --- Logic (for reference) ---
# 1. Sort nums so equal values are adjacent and we can skip duplicates.
# 2. Fix the first index i; we need nums[j] + nums[k] == -nums[i] (a 2Sum on the rest).
# 3. Use two pointers j = i+1, k = n-1: if sum too small move j right, too large move k left.
# 4. When sum == 0, record the triplet, then move both pointers and skip repeated j/k values.
# 5. Skip repeated nums[i] so the same first value does not spawn duplicate triplets.

def threeSum(nums):
    n = len(nums)
    if n < 3:
        return []

    nums.sort()
    result = []

    for i in range(n - 2):
        # Same first element as previous i → would only repeat triplets.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # All remaining numbers are non-negative → sum cannot be 0 with positive nums[i].
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicate second / third values for this fixed i.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]] (typical order after sort)
print(threeSum([0, 1, 1]))  # []
print(threeSum([0, 0, 0]))  # [[0, 0, 0]]

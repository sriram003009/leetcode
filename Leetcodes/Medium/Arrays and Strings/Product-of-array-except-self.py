# Product of Array Except Self
# Return answer where answer[i] equals the product of all nums[j] for j != i.
# Constraints: O(n) time, do not use division.

# Example:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# --- Logic (for reference) ---
# answer[i] = (product of elements left of i) * (product of elements right of i).
# Pass 1 (left to right): store prefix product (everything before i) in answer[i].
# Pass 2 (right to left): multiply answer[i] by a running "suffix" product (everything after i).

def productExceptSelf(nums):
    # Output length matches input; start with 1s so we can multiply into answer later.
    n = len(nums)
    answer = [1] * n

    # Pass 1 — prefix: answer[i] = product of nums[0]..nums[i-1] (empty product = 1 at i=0).
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # Pass 2 — suffix: multiply answer[i] by product of nums[i+1]..end (walk right to left).
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    # Now answer[i] = (left of i) * (right of i) = product of all except nums[i].
    return answer


print(productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print(productExceptSelf([2, 3, 4, 3, 5])) # [180, 120, 90, 120, 72]

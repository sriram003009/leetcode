# Merge Intervals
# Given intervals[i] = [starti, endi], merge every pair that overlaps and return the disjoint union.

# Example:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: [1,3] and [2,6] overlap → [1,6].

# --- Approach (for later review) ---
# Sort intervals by start time. After sorting, any interval that overlaps the running merged block must
# overlap the *last* merged segment (nothing to the left can start after it without being out of order).
# For each [start, end]: if start <= last_merged_end, merge by setting last end to max(last_end, end);
# otherwise push a new interval. Using <= merges touching ranges (e.g. [1,4] and [4,5]).

# --- Complexity (for later review) ---
# Time:  O(n log n) — dominated by sorting n intervals; one O(n) scan after sort.
# Space: O(1) extra if we ignore the output list and sort in-place (output holds merged intervals only).
#        Sorting may use O(log n) stack space depending on the implementation.

def merge(intervals):
    if not intervals:
        return []

    # Same starts can appear in any order; only start time matters for ordering.
    intervals.sort(key=lambda x: x[0])
    merged = [list(intervals[0])]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]
        # Overlap or touch: next begins before or when current block ends.
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
print(merge([[1, 4], [4, 5]]))  # [[1,5]] — touching intervals merge
print(merge([[1, 4], [0, 4]]))  # [[0,4]] — sort pulls [0,4] first

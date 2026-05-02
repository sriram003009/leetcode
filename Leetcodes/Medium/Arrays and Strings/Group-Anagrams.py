# Group Anagrams
# Given an array of strings strs, group anagrams together. Order of groups and order within a group can be any.

# Example:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]  (equivalent groupings / orderings are valid)

# --- Approach (for later review) ---
# Anagrams have the same multiset of letters. Build a canonical key per string:
#   - Count a..z (26 slots) and use tuple(count) as dict key, OR sort the string and use that as key.
#   - Here: counting is O(k) per word of length k (no log k sort).
# Bucket each original string under its key; return all buckets as a list of lists.

# --- Complexity (for later review) ---
# Time:  O(n * k) — n strings, each of length at most k (26-letter count per string).
# Space: O(n * k) — keys and stored strings in the hash map (output size).

from collections import defaultdict


def groupAnagrams(strs):
    groups = defaultdict(list)

    for s in strs:
        # Signature of this word: how many of each letter a..z (LeetCode: lowercase English letters).
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord("a")] += 1
        key = tuple(counts)
        groups[key].append(s)

    return list(groups.values())


example = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(example))
print(groupAnagrams([""]))  # [[""]]
print(groupAnagrams(["a"]))  # [["a"]]

📘 DSA Practice List
🟢 Easy
1. Reverse a Linked List

Problem:
Given the head of a singly linked list, reverse the list and return the reversed list.

2. Detect Cycle in a Linked List

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle.

Explanation:
There is a cycle in a linked list if some node can be reached again by continuously following the next pointer.

Internally, pos denotes the index of the node that the tail’s next pointer connects to.
Note: pos is not passed as a parameter.

🟡 Medium
1. Container With Most Water

Problem:
You are given an integer array height of length n. There are n vertical lines such that the endpoints of the i-th line are (i, 0) and (i, height[i]).

Find two lines that, together with the x-axis, form a container that holds the most water.

Return:
The maximum amount of water the container can store.

Constraint:
You may not slant the container.

2. Find Minimum in Rotated Sorted Array

Problem:
An array sorted in ascending order is rotated between 1 and n times.

Examples:

[4,5,6,7,0,1,2]  // rotated 4 times  
[0,1,2,4,5,6,7]  // rotated 7 times  

Note:
Rotating [a[0], a[1], ..., a[n-1]] once results in:

[a[n-1], a[0], a[1], ..., a[n-2]]

Task:
Given a rotated sorted array of unique elements, return the minimum element.

Requirement:
Time complexity must be O(log n).

3. Longest Repeating Character Replacement

Problem:
You are given a string s and an integer k. You can replace any character in the string with any uppercase English character at most k times.

Return:
The length of the longest substring containing the same letter after performing the operations.

Example:

Input: s = "ABAB", k = 2  
Output: 4  
Explanation: Replace both 'A's with 'B's or vice versa.
4. Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Examples:

Input: s = "abcabcbb"  
Output: 3  
Explanation: "abc" is the longest substring.

Input: s = "bbbbb"  
Output: 1  
Explanation: "b" is the longest substring.
5. Number of Islands

Problem:
Given an m x n 2D binary grid grid representing a map of '1's (land) and '0's (water), return the number of islands.

Explanation:
An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

Example:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

Output: 1
6. Remove Nth Node From End of List

Problem:
Given the head of a linked list, remove the n-th node from the end of the list and return its head.

Examples:

Input: head = [1,2,3,4,5], n = 2  
Output: [1,2,3,5]

Input: head = [1], n = 1  
Output: []

Input: head = [1,2], n = 1  
Output: [1]
7. Palindromic Substrings

Problem:
Given a string s, return the number of palindromic substrings in it.

Definitions:

A string is a palindrome if it reads the same forward and backward.
A substring is a contiguous sequence of characters within a string.

Examples:

Input: s = "abc"  
Output: 3  
Explanation: "a", "b", "c"

Input: s = "aaa"  
Output: 6  
Explanation: "a", "a", "a", "aa", "aa", "aaa"

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters
8. Pacific Atlantic Water Flow

Problem:
Given an m x n grid heights representing an island, determine all coordinates where water can flow to both the Pacific (top & left edges) and Atlantic (bottom & right edges) oceans.

Water can flow to neighboring cells (up, down, left, right) if the neighbor’s height is less than or equal to the current cell.

Return:
A list of coordinates [r, c] where water can flow to both oceans.

Example 1:

Input:
heights = [
 [1,2,2,3,5],
 [3,2,3,4,4],
 [2,4,5,3,1],
 [6,7,1,4,5],
 [5,1,1,2,4]
]

Output:
[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:

Input: heights = [[1]]  
Output: [[0,0]]

Constraints:

1 <= m, n <= 200
0 <= heights[r][c] <= 10^5
🔴 Hard
1. Minimum Window Substring

Problem:
Given two strings s and t of lengths m and n, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.

If no such substring exists, return an empty string "".

Note:
Test cases are generated such that the answer is unique.

Examples:

Input: s = "ADOBECODEBANC", t = "ABC"  
Output: "BANC"

Input: s = "a", t = "a"  
Output: "a"

Input: s = "a", t = "aa"  
Output: ""  
Explanation: Not enough 'a's in s to cover t.

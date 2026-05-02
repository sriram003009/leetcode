# Valid Parentheses
# Given a string of '(', ')', '{', '}', '[' and ']', return True iff every bracket is closed by the same type in the correct order.

# Example:
# Input: s = "()"
# Output: True
# Input: s = "()[]{}"
# Output: True
# Input: s = "(]"
# Output: False

# --- Logic (for reference) ---
# 1. Scan left to right. Track "still open" brackets with a stack (LIFO = last opened closes first).
# 2. Opening chars '(', '{', '[' → push onto stack (we expect a matching closer later).
# 3. Closing chars ')', '}', ']' → must match the *most recent* unmatched opener (stack top).
#    - Pop the top; if stack empty or top != expected opener for this closer → invalid.
# 4. After the string, stack must be empty (every opener was closed).

def isValid(s: str) -> bool:
    # Map each closer to the opener it must pair with
    close_to_open = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c in close_to_open:
            # Closer: need a matching opener on top of stack
            if not stack or stack.pop() != close_to_open[c]:
                return False
        else:
            # Opener: defer matching until we see the right closer
            stack.append(c)
    # Any leftover openers means unclosed brackets
    return len(stack) == 0


print(isValid("()"))  # True
print(isValid("()[]{}"))  # True
print(isValid("(]"))  # False
print(isValid("([)]"))  # False
print(isValid("{[]}"))  # True

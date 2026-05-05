def max_cyclic_substring_sum(s):
    n = len(s)
    doubled = s + s

    left = 0
    current_sum = 0
    max_sum = 0

    char_index = {}

    for right in range(len(doubled)):
        ch = doubled[right]
        value = ord(ch) - ord('a') + 1

        # If duplicate character exists in current window
        while ch in char_index and char_index[ch] >= left:
            remove_char = doubled[left]
            current_sum -= ord(remove_char) - ord('a') + 1
            left += 1

        # Window size should not exceed original string length
        while right - left + 1 > n:
            remove_char = doubled[left]
            current_sum -= ord(remove_char) - ord('a') + 1
            left += 1

        current_sum += value
        char_index[ch] = right

        max_sum = max(max_sum, current_sum)

    return max_sum


# Input
s = input().strip()

# Output
print(max_cyclic_substring_sum(s))
# ...
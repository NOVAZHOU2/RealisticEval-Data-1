from collections import Counter
from typing import Optional


def find_min_window_substring(source: str, target: str) -> Optional[str]:
    """
    Finds the smallest window in the source string that contains all characters of the target string.

    Args:
        source (str): The source string in which to search for the window.
        target (str): The target string containing the characters to be matched.

    Returns:
        Optional[str]: The smallest window in the source string that contains all characters of the target string.
                       Returns an empty string if no such window exists.
    """
    if not source or not target:
        return ''

    # Count the frequency of characters in the target string
    required_chars = Counter(target)
    # Counter to track characters in the current window of the source string
    window_chars = Counter()

    left = 0  # Left boundary of the window
    min_length = float('inf')  # Initialize the minimum length as infinity
    min_window = ''  # Initialize the minimum window string

    # Iterate over the source string with the right boundary of the window
    for right, char in enumerate(source):
        if char in required_chars:
            window_chars[char] += 1

        # Check if the current window contains all characters of the target string
        while all(window_chars[c] >= required_chars[c] for c in required_chars):
            window_size = right - left + 1
            if window_size < min_length:
                min_length = window_size
                min_window = source[left:right + 1]

            # Attempt to shrink the window from the left
            left_char = source[left]
            if left_char in required_chars:
                window_chars[left_char] -= 1
            left += 1

    return min_window if min_length <= len(source) else ''

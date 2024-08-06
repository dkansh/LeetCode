class Solution(object):
    def minimumPushes(self, word):
        # Initialize a frequency array
        frequency = [0] * 26

        # Count character frequencies
        for char in word:
            frequency[ord(char) - ord('a')] += 1

        # Sort the frequency array
        frequency.sort()

        # Initialize variables for key press assignment
        i = 25
        count = 0
        multiplier = 1
        result = 0

        # Assign key presses based on frequency
        while i >= 0 and frequency[i] != 0:
            result += (multiplier * frequency[i])
            count += 1
            if count == 8:
                multiplier += 1
                count = 0
            i -= 1

        # Return the total key presses
        return result

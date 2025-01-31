class Solution(object):
    def __init__(self):
        self.dict = {}
        self.max = 0
    
    def add_char(self, char):
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
        
        self.max = max(self.max, self.dict[char])
    
    def remove_char(self, char):
        if char in self.dict:
            self.dict[char] -= 1
        
        max = 0
        for keys in self.dict:
            if self.dict[keys] > max:
                max = self.dict[keys]
        
        self.max = max


    def characterReplacement(self, s, k):
        left = 0
        max_count = 0  # Tracks the count of the most frequent character in the current window
        freq_map = defaultdict(int)
        max_len = 0
        
        for right in range(len(s)):
            # Add the current character to the frequency map
            freq_map[s[right]] += 1
            
            # Update the max_count to the highest frequency in the current window
            max_count = max(max_count, freq_map[s[right]])
            
            # If the window size minus the count of the most frequent character is more than k,
            # we shrink the window from the left.
            if (right - left + 1) - max_count > k:
                freq_map[s[left]] -= 1
                left += 1
            
            # Update the maximum length of the window
            max_len = max(max_len, right - left + 1)
        
        return max_len

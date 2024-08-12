class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_count = Counter(t)
        left, right = 0, 0
        required_chars = len(t)
        min_len = float('inf')
        min_window_start = 0

        while right < len(s):
            if t_count[s[right]] > 0:
                required_chars -= 1
            t_count[s[right]] -= 1
            right += 1
            while required_chars == 0:
                if right - left < min_len:
                    min_len = right - left
                    min_window_start = left
                t_count[s[left]] += 1
                if t_count[s[left]] > 0:
                    required_chars += 1
                left += 1
        return "" if min_len == float('inf') else s[min_window_start:min_window_start + min_len]
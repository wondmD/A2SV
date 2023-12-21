class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            current_value = roman_values[s[i]]
            if i < n - 1:
                next_value = roman_values[s[i + 1]]
                if current_value < next_value:
                    total -= current_value
                else:
                    total += current_value
            else:
                total += current_value

        return total
        
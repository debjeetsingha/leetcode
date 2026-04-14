class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        val=0
        last_digit=0
        for sym in s[::-1]:
            new_val = sym_val[sym]
            if new_val<last_digit:
                val=val-new_val
            else:
                val=val+new_val
            last_digit=new_val
        return val

        
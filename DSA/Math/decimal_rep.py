class Solution(object):
    def decimalRepresentation(self, n):
        ans = []
        p = 0
        while n > 0:
            d = n % 10
            if d:
                ans.append(d * (10 ** p))
            n //= 10
            p += 1
        ans.sort(reverse=True)
        return ans

        

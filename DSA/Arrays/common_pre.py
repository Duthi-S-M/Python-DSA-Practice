class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return " "

        pre = strs[0] # in the string 1st word is considered as strs[0] (flower)

        for i in strs[1:]:
            while not i.startswith(pre):  # does flow starts with pre(flower)
                pre = pre[:-1]  # flowe --> flow 
            if pre == " ":
                    return " "
        return pre         

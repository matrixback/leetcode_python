class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, col_strs in enumerate(zip(*strs)):
            if len(set(col_strs)) > 1:
                return strs[0][:i]
        return min(strs)
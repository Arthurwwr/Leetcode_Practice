class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def backtrack(left, right, path):
            if len(path) == 2 * n:
                result.append(path)
                return
            if left < n:
                backtrack(left + 1, right, path + '(')
            if right < left:
                backtrack(left, right + 1, path + ')')
        backtrack(0, 0, '')
        return result

sol = Solution()
print(sol.generateParenthesis(3))
# T: O(log10n)
# S: O(n)
class Solution:
  def three_eight_six_1(self, n):
    res = []

    def dfs(cur):
      if cur > n:
        return
      
      res.append(cur)
      cur *= 10
      for i in range(10):
        dfs(cur + 1)

      for i in range(1, 10):
        dfs(i)
      
      return res
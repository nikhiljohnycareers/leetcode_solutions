# T: O(log10n)
# S: O(1)
class Solution:
  def three_eight_six_2(self, n):
    res = []

    cur = 1
    while len(res) < n:
      res.append(cur)
      

      if cur * 10 <= n:
        cur *= 10
      else:
        while cur == n or cur % 10 == 9:
          cur //= 10
        
        cur += 1

    return res
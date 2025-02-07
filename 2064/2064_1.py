class Solution:
  def two_zero_six_four_1(self, n, quantities):
    def can_distribute(x):
      stores = 0
      for q in quantities:
        stores += math.ceil(q / x)
      
      return stores <= n

    l, r = 1, max(quantities)

    res = 0
    while l <= r:
      mid = (l + r) // 2
      if can_distribute(mid):
        res = mid
        l = mid - 1
      else:
        r = mid + 1
      
    return res
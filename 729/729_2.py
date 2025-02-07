# T: O(logn)
# S: O(n)

class TreeNode:
  def __init__(self, start, end) -> None:
    self.left = None
    self.right = None
    self.start = start
    self.end = end

  def insert(self, start, end) -> bool:
    cur = self
    while True:
      if start >= cur.end:
        if not cur.right:
          cur.right = TreeNode(start, end)
          return True
        cur = cur.right
      elif end <= cur.start:
        if not cur.left:
          cur.left = TreeNode(start, end)
          return True
        cur = cur.left
      else:
        return False

class Solution:
  def __init__(self) -> None:
    self.root = None

  def book(self, start: int, end: int) -> bool:
    if not self.root:
      self.root = TreeNode(start, end)
      return True
    
    return self.root.insert(start, end)

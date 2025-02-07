# T: O(n)
# S: O(n)
class Solution:
  def __init__(self) -> None:
    self.events = []

  def book(self, start: int, end: int) -> bool:
    for s, e in self.events:
      if start < e and end > s:
        return False
    
    self.events.append((start, end))
    return True
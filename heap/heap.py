import math
class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    index = len(self.storage)-1
    self._bubble_up(index)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    if (index == 1):# root, done
        return
    # compare with the parent and swap place if bigger
    parent_index = math.floor(index/2)
    parent = self.storage[parent_index]
    if (parent < self.storage[index]):
        self.storage[parent_index] = self.storage[index] 
        self.storage[index] = parent
    self._bubble_up(parent_index)
        
  def _sift_down(self, index):
    pass

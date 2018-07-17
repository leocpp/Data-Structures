class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if (self.value == None):
        self.value = BinarySearchTree(value)
    elif (value < self.value):
        if (self.left == None):
            self.left = BinarySearchTree(value)
        else:
            self.left.insert(value)
    else:
        if (self.right == None):
            self.right = BinarySearchTree(value)
        else:
            self.right.insert(value)
         

  def contains(self, target):
    if (self.value == target):
        return True 
    elif (target < self.value and self.left != None):
        return self.left.contains(target)
    elif (self.right != None):
        return self.right.contains(target)
    else:
        return False
        

  def get_max(self):
    max = self.value
    p = self.right
    while (p != None):
        max = p.value
        p = p.right
    return max

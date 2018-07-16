"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):

    node = Node()
    node.value = value
    
    if self.head == None: # if list is empty
      self.head = node
      self.tail = node
    else:
      assert(self.tail.next_node == None)
      self.tail.next_node = node
      self.tail = node


  def remove_head(self):
    value = None
    if self.head != None:
        value = self.head.value
        self.head = self.head.next_node
    return value

  def contains(self, value):
    p = self.head
    found = False
    if (p != None):
        while True:
            if p.value == value:
                found = True
                break
            else: 
                if p.next_node != None:
                    p = p.next_node
                else:
                    break;
    return found
            
        

  def get_max(self):
    max_value = None
    if self.head != None:
        max_value = self.head.value
        p = self.head
        while p.next_node != None:
            if max_value < p.next_node.value:
               max_value = p.next_node.value
            p = p.next_node
    return max_value
     

#################################################################################################
#  This code compares a nested function with small "class version" of the same implementation.  #
#  Conclusion : In Python, use class instead of nested function!                                #
#  Python : 3.x                                                                                 #
#################################################################################################

################## Class version
class Trace:
  nodes, edges = set(), set()

  def build(self, v):
    if v not in self.nodes:
      self.nodes.add(v)
      for child in v._prev:
        self.edges.add((child, v))
        self.build(self, child)
  def __new__(self, root):
    self.build(self, root)
    return self.nodes, self.edges
print("Class 2:", timeit.timeit("Trace(r)", setup="from __main__ import Trace, r"))

################## Nested function version
def trace(root):
  nodes, edges = set(), set()
  def build(v):
    if v not in nodes:
      nodes.add(v)
      for child in v._prev:
        edges.add((child, v))
        build(child)
  build(root)
  return nodes, edges
print("Nested function:", timeit.timeit("trace(r)", setup="from __main__ import trace, r"))

################## Result
# Simple class: 0.2400555419999364
# Nested function: 1.5396377079996455

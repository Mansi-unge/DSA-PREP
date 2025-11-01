# Single Responsibility Principle

# bad example 
"""
class report :
  def print_report(): pass
  def geneerate(): pass
"""

# good example 

class generate_report:
  def generate(self): pass

class print_report:
  def print_report(self): pass

  
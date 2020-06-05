# Create a file called item.py and add an Item class in there.

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

class RoomItem:
  def __init__(self, name=None, description=None):
    self.name = name
    self.description = description
  def on_take(self):
    print("You have picked up:", self.name)
  def on_drop(self):
    print("You have dropped:", self.name)
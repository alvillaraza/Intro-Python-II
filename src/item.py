# Create a file called item.py and add an Item class in there.

# The item should have name and description attributes.

# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.

class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

# item = {
#   'backpack': Item('Backpack', 'used for storing items'),
#   'shovel': Item('Shovel', 'used for digging'),
#   'key': Item('Key', 'used for opening locks'),
#   # 'backpack': {
#   #   name: 'Backpack',
#   #   desc: 'used for storing items'
#   # }
# }
# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, has_item=None):
    self.name = name
    self.current_room = current_room
    self.has_item = PlayerItem(has_item)

class PlayerItem:
    def __init__(self, has_item):
        self.has_item = has_item

#items: backpack, shovel, key
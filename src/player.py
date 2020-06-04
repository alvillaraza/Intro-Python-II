# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room, list_item):
    self.name = name
    self.current_room = current_room
    self.list = PlayerList(list_item)

class PlayerList:
    def __init__(self, item):
        self.item = item

#items: backpack, shovel, key
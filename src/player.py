# Write a class to hold player information, e.g. what room they are in
# currently.
from item import RoomItem
from room import Room

class Player:
  def __init__(self, name, current_room, has_item="this one?"):
    self.name = name
    self.current_room = current_room
  def get_item(self, item):
    self.has_item = item
    self.has_item.on_take()
  


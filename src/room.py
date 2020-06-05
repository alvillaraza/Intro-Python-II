# Implement a class to hold room information. This should have name and
# description attributes.

from item import RoomItem


class Room:
    def __init__(self, name, desc, item=None):
        self.name = name
        self.desc = desc
        self.item = [RoomItem(item)]
    def remove_item(self):
        self.item = RoomItem()
    def add_item(self, item):
        self.item = item


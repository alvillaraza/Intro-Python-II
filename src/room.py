# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, desc, item=None):
        self.name = name
        self.desc = desc
        self.item = RoomItem(item)


class RoomItem:
    def __init__(self, item):
        self.item = item


"""
Lab_4, Task_6, MODULE WITH CLASSES (LOCATIONS)
"""


class Street:
    """
    The class do create street
    """

    def __init__(self, street_name: str):
        """
        The func set param
        :param street_name: name of street
        :param description: description of street
        """
        self.description = ''
        self.street_name = street_name
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def get_name(self) -> str:
        """
        The func get name of street
        :return: name
        """
        return self.street_name

    def get_description(self) -> str:
        """
        The func get description of street
        :return: string
        """
        return self.description

    def set_description(self, description: str):
        """
        The func do something
        :param description:
        :return:
        """
        self.description = description

    def set_character(self, character):
        """
        Te function set character
        :param character:
        :return:
        """
        self.character = character

    def get_character(self):
        """
        The func return character
        :return:
        """
        return self.character

    def link_room(self, linked_room, direction: str):
        """
        The func do something
        :return:
        """
        self.linked_rooms.update({linked_room: direction})

    def get_details(self):
        """
        The func do something
        :return:
        """
        print(self.street_name)
        print("--------------------")
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {self.street_name} is {self.linked_rooms[direction]}")

    def set_item(self, item):
        """
        The func set rooms
        :return:
        """
        self.item = item

    def get_item(self):
        """
        The function return something
        :return:
        """
        return self.item

    def move(self, direction: str):
        """
        The function do something
        :return:
        """
        for i in self.linked_rooms.items():
            if i[1] == direction:
                return i[0]
        return self


class Building(Street):
    """
    Class create buildings
    """

    def __init__(self, street_name: str, description: str, building_name: str):
        super().__init__(street_name, description)
        self.building_name = building_name





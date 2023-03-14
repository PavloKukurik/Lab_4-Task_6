"""
Lab_4, Task_6, MODULE WITH CLASSES (ITEMS)
"""


class Item:
    """
    Thr class create items for player
    """

    def __init__(self, name: str):
        """
        The func set param
        """
        self.name = name
        self.description = ''

    def get_name(self):
        """
        The func return name
        :return:
        """
        return self.name

    def set_description(self, description):
        """
        The func do something
        :param description:
        :return:
        """
        self.description = description

    def get_description(self):
        """
        The fun return description
        :return:
        """
        return self.description

    def describe(self):
        """
        The func do something
        :return:
        """
        print(f'The {self.name} is here - {self.description}')


class Potion(Item):
    """
    The class create poison
    """

    def __init__(self, name, effect):
        """
        The func set methods
        :param name: name of poison
        :param effect: effect by poison
        """
        super().__init__(name)
        self.effect = effect

    def use(self, target):
        """
        The func do something
        :param target:
        :return:
        """
        print(f"Using {self.name} potion...")
        self.effect(target)

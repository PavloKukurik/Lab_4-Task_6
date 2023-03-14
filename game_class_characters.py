"""
Lab_4, Task_6, MODULE WITH CLASSES (CHARACTERS)
"""


class Character:
    """
    The class create character
    """

    def __init__(self, name: str, description: str):
        """
        The func set param
        :param name: name of character
        :param description: description of character
        """
        self.description = description
        self.name = name
        self.conversation = None

    def get_name(self) -> str:
        """
        The func get name of character
        :return: name
        """
        return self.name

    def get_description(self) -> str:
        """
        The func get description of street
        :return: string
        """
        return self.description

    def set_conversation(self, conversation: str):
        """
        The func set conversation of character
        :param conversation: Phrase of character
        :return: string
        """
        self.conversation = conversation

    def talk(self):
        """
        The func determine what character need to talk
        :return: string
        """
        print(f"[{self.name} says]: {self.conversation}")

    def describe(self):
        """
        The func do something
        :return:
        """
        print(f'The {self.name} is here - {self.description}')


class Player(Character):
    """
    The class create main character (player)
    """

    def __init__(self, name: str, description: str, health: int, attach: int):
        super().__init__(name, description)
        self.attach = attach
        self.health = health

    def talk_to_other(self, conversation):
        """
        The func do something
        :param conversation:
        :return:
        """
        print(f"[{self.name} says:] : {conversation}")


class FriendTrader(Character):
    """
    The class create friend
    """

    def __init__(self, name: str, description: str):
        super().__init__(name, description)
        self.hint = ''
        self.goods = ''

    def set_help(self, hint: str):
        """
        the func return hint (help for player)
        :param hint: hint for player
        :return:
        """
        self.hint = hint

    def set_trade(self, goods):
        """
        The func set item for trade
        :param goods: goods for trade
        :return: None
        """
        self.goods = goods


class Enemy(Character):
    """
    The class create enemy
    """

    def __init__(self, name: str, description: str, health: int, attach: int):
        """
        The func set param
        :param name: name of enemy
        :param description: description of enemy
        :param health: health of enemy
        :param attach: attach damage
        """
        super().__init__(name, description)
        self.attach = attach
        self.health = health
        self.weakness = None
        self.conversation = None

    def set_weakness(self, weakness: str):
        """
        The func find weakness of enemy
        :return:
        """
        self.weakness = weakness

    def fight(self, fight_with):
        """
        The function do something
        :return:
        """
        return self.weakness == fight_with


class Moscal(Enemy):
    """
    Tha class create unique enemy
    """
    def __init__(self, name: str, description: str, health=0, attach=0):
        super().__init__(name, description, health, attach)
        self.conversation = "ААА, Дамбілі Бамбас восємь лєт"
        self.weakness = "Сало"

    def get_def(self, weakness):
        """
        The func determine if moscal is dead
        :param weakness:
        :return:
        """
        return self.weakness == weakness


# char = Friend("Бандера", "Їсть москалоту на сніднок")
# char.set_conversation("Nam nam nam, hail gitler")
# print(char.talk())

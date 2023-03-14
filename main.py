"""
Lab_4,Task_6, MAIN_MODULE
"""

import game_class_locations
import game_class_characters
# import game_class_items

# Create locations for game
university = game_class_locations.Street("УКУ")
university.set_description("Сучасний та просторий університет")

park = game_class_locations.Street("Стрийський парк")
park.set_description("Великий та затишний парк недалеко від центру міста")

prospectus_of_liberty = game_class_locations.Street("Проспект Свободи")
prospectus_of_liberty.set_description("Головний проспект Львова, де трапляється багато цікавих речей")

square = game_class_locations.Street("Площа ринок")
square.set_description("Мальовнича площа, з гарними будинками")


university.link_room(park, "north")
park.link_room(university, "south")
park.link_room(prospectus_of_liberty, "north")
prospectus_of_liberty.link_room(park, "south")
prospectus_of_liberty.link_room(square, "east")
square.link_room(prospectus_of_liberty, "west")

# moscal = game_class_characters.Moscal("Русня", "Свинособака")
student = game_class_characters.Character('Микола', "Студен факультету прикладих наук")
student.set_conversation("Удачі вам у дорозі")
university.set_character(student)

homeless = game_class_characters.FriendTrader("Безхатько", "Добрий та вихований дядько")
homeless.set_conversation("Москалів можна перемогти або салом, або сказати 'Слава Укаїні'")
park.set_character(homeless)

moscal = game_class_characters.Moscal("Москаль", "Смедючий кусок лайна")
park.set_character(moscal)


current_room = university
backpack = []

dead = False

# while True:
#     current_room.get_details()
#
#     inhabitant = current_room.get_character()
#     if inhabitant is not None:
#         inhabitant.describe()
#
#     item = current_room.get_item()
#     if item is not None:
#         item.describe()
#
#     command = input(">>> ")
#
#     if command in ["north", "south", "east", "west"]:
#         current_room = current_room.move(command)
#
#     elif command == "talk":
#         if inhabitant is not None:
#             inhabitant.talk()
#
#     elif command == "fight":
#         if inhabitant is not None:
#             # Fight with the inhabitant, if there is one
#             print("What will you fight with?")
#             fight_with = input()
#
#             # Do I have this item?
#             if fight_with in backpack:
#
#                 if inhabitant.fight(fight_with) is True:
#                     # What happens if you win?
#                     print("Hooray, you won the fight!")
#                     current_room.character = None
#                     if inhabitant.get_defeated() == 2:
#                         print("Congratulations, you have vanquished the enemy horde!")
#                         dead = True
#                 else:
#                     # What happens if you lose?
#                     print("Oh dear, you lost the fight.")
#                     print("That's the end of the game")
#                     dead = True
#             else:
#                 print("You don't have a " + fight_with)
#         else:
#             print("There is no one here to fight with")
# while dead is False:
#
#     print("\n")
#     current_room.get_details()
#
#     inhabitant = current_room.get_character()
#     if inhabitant is not None:
#         inhabitant.describe()
#
#     item = current_room.get_item()
#     if item is not None:
#         item.describe()
#
#     command = input("> ")
#
#     if command in ["north", "south", "east", "west"]:
#         # Move in the given direction
#         current_room = current_room.move(command)
#     elif command == "talk":
#         # Talk to the inhabitant - check whether there is one!
#         if inhabitant is not None:
#             inhabitant.talk()
#     elif command == "fight":
#         if inhabitant is not None:
#             # Fight with the inhabitant, if there is one
#             print("What will you fight with?")
#             fight_with = input()
#
#             # Do I have this item?
#             if fight_with in backpack:
#
#                 if inhabitant.fight(fight_with) is True:
#                     # What happens if you win?
#                     print("Hooray, you won the fight!")
#                     current_room.character = None
#                     if inhabitant.get_defeated() == 2:
#                         print("Congratulations, you have vanquished the enemy horde!")
#                         dead = True
#                 else:
#                     # What happens if you lose?
#                     print("Oh dear, you lost the fight.")
#                     print("That's the end of the game")
#                     dead = True
#             else:
#                 print("You don't have a " + fight_with)
#         else:
#             print("There is no one here to fight with")
#     elif command == "take":
#         if item is not None:
#             print("You put the " + item.get_name() + " in your backpack")
#             backpack.append(item.get_name())
#             current_room.set_item(None)
#         else:
#             print("There's nothing here to take!")
#     else:
#         print("I don't know how to " + command)

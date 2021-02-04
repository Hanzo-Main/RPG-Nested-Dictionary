# Course: CS 30
# Period: 1
# Date created: 21/01/28
# Date last modified: 21/02/04
# Name: Kira Gray
# Description: RPG nested dictionary for characters, locations, and inventory.

# a nested dictionary of locations in the game
locations = {
  'cargo_left': {
    'size': 'large',
    'apperence': 'many crates are piled high',
    'next_places': """there is more cargo on the right and a latter going up on
    the left"""
  },
  'cargo_right': {
    'size': 'large',
    'apperence': """more cargo containers""",
    'next_places': """theres a door to the right and the other side of the cargo
    hold on the left"""
  },
  # may not be in the final cut
  'hypdriv_room': {
    'size': 'tiny',
    'apperence': """the hyperdrive, with two pirates""",
    'next_places': 'the only way is to the cargo hold on the left'
  },
  'crew_quarts': {
    'size': 'small',
    'apperence': """there is a table and beds. There are two pirates""",
    'next_places': 'the only way is right to the latter going down',
  },
  'living_area': {
    'size': 'medium',
    'apperence': """typical living arrangements. There are three pirates""",
    'next_places': """the latter going down to the cargo is on the left and
    a latter going up on the right""",
  },
  # may not be in the final cut
  'caps_quarts': {
    'size': 'small',
    'apperence': """normal single bedroom, with a crate against the bed""",
    'next_places': """the only way is to the right to the latter going to the
    living area""",
  },
  'locked_room': {
    'size': 'tiny',
    'apperence': """nothing in it, it's just a room leading to the cockpit""",
    'next_places': """the latter going to the living area is on the left and the
    cockpit is to the right""",
  },
  'cockpit': {
    'size': 'medium',
    'apperence': 'three pirates and the captain, everything else is normal',
    'next_places': 'the only way is to the left back to the small room'
  }
}

# for loop that print the locations and information about it
print("The details of the loctions in the game: ")
for location, places in locations.items():
    size = places['size']
    apperence = places['apperence']
    next_places = places['next_places']
    print(f"""\n{location.title()} is a {size} room. There is {apperence}.
    {next_places}""")

# a nested dictionary of characters in the game and information on them.
characters = {
  'player': {
    'descr': 'the character you play as',
    'dmg': '50',
    'health': '100'
  },
# I imagine im going to have to make multiple clones of this guy, but for now
# im sticking with only writing the one. 8 for sure, 10 if i keep the hyperdrive room.
  'pirate': {
    'descr': 'a basic pirate gumby',
    'dmg': '25',
    'health': '50'
  },
  'captain': {
    'descr': 'the pirate captain, the one calling the shots',
    'dmg': '50',
    'health': '150'
  }
}

# for loop that prints off the characters in the game and information on them
# if else statement to give player more personalized info
print("""
""")
print("\nThe details of the characters in the game:")
for character, info in characters.items():
  descr = info['descr']
  dmg = info['dmg']
  health = info['health']
  if character == 'player':
    print(f"""\n{character.title()} is {descr}. 
    Your blaster deals {dmg} and you have {health} health.""")
  else:
    print(f"""\n{character.title()} is {descr}. 
    Thier blaster deals {dmg} and they have {health} health.""")

# a dictionary of items that the charactrs have in thier inventory (at the start)
print("""
""")
print("\nThe idventorys of the characters in the game:")
inventory = {
  'player': ['blaster'],
  'pirate': ['blaster', 'health kit'],
  'captain': ['blaster', 'override card'],
}

# for loops that prints off the diffrent characters inventory
for inven, items in inventory.items():
  print(f"\n {inven.title()}'s inventory:")
  for item in items: 
    print(f"\t{item}")

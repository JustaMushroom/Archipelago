from BaseClasses import Item, ItemClassification
from typing import TypedDict

class RobobeatItem(Item):
    game = "ROBOBEAT"

class RobobeatItemData(TypedDict):
    name: str
    type: BaseClasses.ItemClassification
    count: int = 1


all_items = [
    {'name': "Progressive Key",
     'type': ItemClassification.progression,
     'count': 3},
    {'name': "Shop Room Blueprint",
     'type': ItemClassification.progression},
    {'name': "Parkour Room Blueprint",
     'type': ItemClassification.progression}
    {'name': "Directional Bomb Blueprint",
    'type:': ItemClassification.useful}
    {'name': "Hammer Blueprint",
    'type:': ItemClassification.useful}
    {'name': "Bouncer Blueprint",
    'type:': ItemClassification.useful}
    {'name': "Comeback Blueprint",
    'type:': ItemClassification.useful}
    {'name': "Hook Shot Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Flare Gun Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Deploy Turret Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Bullethell Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Tempo Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Cosmic Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Replica Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Nuke Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Yojimbo Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Knife Throw Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Virus Room Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Clockwork Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Infinite Locker Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Dunker Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "The Finish Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Faulty Double Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Magnet Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Stab Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Fire Bomb Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Nexus Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Volt Impact Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Target Rush Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Boombox Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Freeze Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Nocap Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Rapid Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Axe Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Crossbow Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Echo Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Card Shark Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Shield Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Da Capo Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Daredevil Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "Curveball Blueprint",
    'type:':  ItemClassification.useful}
    {'name': "30 Blips",
    'type:':  ItemClassification.filler}
    {'name': "3000 Credits",
    'type:':  ItemClassification.filler}
]

filler_items = ["30 Blips", "3000 Credits"]

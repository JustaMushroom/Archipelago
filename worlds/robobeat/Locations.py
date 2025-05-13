from BaseClasses import Location
from typing import Dict, List


class RobobeatLocation(Location):
    game = "ROBOBEAT"


all_locations = [
    "Directional Bomb Blueprint",
    "Hammer Blueprint",
    "Bouncer Blueprint",
    "Armory Key",
    "Comeback Blueprint",
    "Hook Shot Blueprint",
    "Flare Gun Blueprint",
    "Deploy Turret Blueprint",
    "Bullethell Blueprint",
    "Tempo Blueprint",
    "Cosmic Blueprint",
    "Heartstopper Blueprint",
    "Nuke Blueprint",
    "Yojimbo Blueprint",
    "Knife Throw Blueprint",
    "Virus Room Blueprint",
    "Clockwork Blueprint",
    "Infinite Locker Blueprint",
    "Dunker Blueprint",
    "The Finish Blueprint",
    "Faulty Double Blueprint",
    "Magnet Blueprint",
    "Stab Blueprint",
    "Fire Bomb Blueprint",
    "Nexus Blueprint",
    "Volt Impact Blueprint",
    "Target Rush Room Blueprint",
    "Study Key",
    "Boombox Blueprint",
    "Freeze Blueprint",
    "Nocap Blueprint",
    "Rapid Blueprint",
    "Axe Blueprint",
    "Crossbow Blueprint",
    "Frazzer's Room Key",
    "Echo Blueprint",
    "Card Shark Blueprint",
    "Shield Blueprint",
    "Da Capo Blueprint",
    "Shop Room Blueprint",
    "Parkour Room Blueprint",
    "Replica Blueprint",
    "Curveball Blueprint",
    "Defeat Ray Punk",
    "Defeat The Showman",
    "Defeat The Mask",
    "Defeat Frazzer",
    "Complete Communications",
    "Complete The Armory",
    "Complete The Study",
]



location_regions: Dict[str, List[str]] = {
    "The HUB": ["Directional Bomb Blueprint", "Hammer Blueprint"],
    "Communications": ["Bouncer Blueprint", "Armory Key", "Complete Communications"],
    "The Old Passage": ["Comeback Blueprint", "Hook Shot Blueprint", "Flare Gun Blueprint", "Deploy Turret Blueprint", "Tempo Blueprint", "Cosmic Blueprint", "Heartstopper Blueprint", "Shop Room Blueprint", "Parkour Room Blueprint"],
    "The Gallery": ["Nuke Blueprint", "Yojimbo Blueprint", "Knife Throw Blueprint", "Virus Room Blueprint", "Clockwork Blueprint", "Infinite Locker Blueprint", "Replica Blueprint", "Defeat Ray Punk"],
    "The Ruins": ["Dunker Blueprint", "The Finish Blueprint", "Faulty Double Blueprint", "Magnet Blueprint", "Stab Blueprint", "Fire Bomb Blueprint", "Nexus Blueprint", "Volt Impact Blueprint", "Target Rush Room Blueprint", "Study Key", "Curveball Blueprint", "Defeat The Showman", "Complete The Armory"],
    "The Citadel": ["Boombox Blueprint", "Freeze Blueprint", "Nocap Blueprint", "Rapid Blueprint", "Axe Blueprint", "Crossbow Blueprint", "Frazzer's Room Key", "Defeat The Mask", "Complete The Study"],
    "The Machine": ["Echo Blueprint", "Card Shark Blueprint", "Shield Blueprint", "Da Capo Blueprint", "Defeat Frazzer"]
}

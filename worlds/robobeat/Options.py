from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions, DefaultOnToggle, Visibility, OptionList
from dataclasses import dataclass

class RandomizeStartingLoadout(Toggle):
    """Randomizes the 4 starting weapons (Revolver, Flux, Contact, Ping Pong) + the 2 starting utilities (Teleport, Lightning Strike)
    Currently not implemented"""
    display_name = "Randomize Starting Loadout"

class RandomizedLoadout(OptionList):
    display_name = "Starting Loadout"
    visibility = Visibility.spoiler
    default = set(["Revolver", "Flux", "Contact", "Ping Pong", "Teleport", "Lightning Strike"])

class Blueprintsanity(Toggle):
    """Add blueprint unlocks to the pool, doubles the number of blueprint checks
    Currently not implemented"""

@dataclass
class RobobeatOptions(DeathLinkMixin, PerGameCommonOptions):
    randomize_starting_loadout: RandomizeStartingLoadout
    randomized_loadout: RandomizedLoadout

from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions, DefaultOnToggle

class RandomizeStartingLoadout(Toggle):
    """Randomizes the 4 starting weapons (Revolver, Flux, Contact, Ping Pong) + the 2 starting utilities (Teleport, Lightning Strike)
    Currently not implemented"""
    display_name = "Randomize Starting Loadout"
    default = False

class Blueprintsanity(Toggle):
    """Add blueprint unlocks to the pool, doubles the number of blueprint checks
    Currently not implemented"""

@dataclass
class RobobeatOptions(DeathLinkMixin, PerGameCommonOptions):
    randomize_starting_loadout: RandomizeStartingLoadout

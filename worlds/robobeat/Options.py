from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions, DefaultOnToggle

class RandomizeStartingLoadouts(Toggle):
    """Randomizes the 4 starting weapons (Revolver, Flux, Contact, Ping Pong) + the 2 starting utilities (Teleport, Lightning Strike)"""
    display_name = "Randomize Starting Loadout"

@dataclass
class RobobeatOptions(PerGameCommonOptions):
    pass

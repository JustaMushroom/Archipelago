from typing import TYPE_CHECKING, Dict, Callable
from BaseClasses import CollectionState, LocationProgressType

if TYPE_CHECKING:
    from . import RobobeatWorld
else:
    RobobeatWorld = object


class RobobeatRules:
    player: int
    world: RobobeatWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: RobobeatWorld):
        self.player = world.player
        self.world = world
        self.location_rules = {}
        self.region_rules = {
            "The Old Passage": self.armory_access,
            "The Gallery": self.armory_access,
            "The Ruins": self.armory_access,
            "The Citadel": self.study_access,
            "The Machine": self.frazzer_access,
        }
        self.location_rules = {
            "Parkour Room Blueprint": self.shop_access,
            "Curveball Blueprint": self.parkour_access,
            "Stab Blueprint": self.has_contact
        }

    def armory_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player)

    def study_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, 2)

    def frazzer_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, 3)

    def shop_access(self, state: CollectionState) -> bool:
        return state.has("Shop Room Blueprint", self.player)

    def parkour_access(self, state: CollectionState) -> bool:
        return state.has("Parkour Room Blueprint", self.player)

    def has_contact(self, state: CollectionState) -> bool:
        # return state.has("Contact Blueprint", self.player)
        return True if "Contact" in self.world.options.randomized_loadout.value else state.has("Contact Blueprint", self.player)

    def set_all_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]

            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]


        # from Utils import visualize_regions
        # visualize_regions(multiworld.get_region("The HUB", self.player), "my_world.puml")

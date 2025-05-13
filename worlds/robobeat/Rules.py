from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import RobobeatWorld
else:
    RobobeatWorld = object


class RobobeatRules:
    player: int
    world: RobobeatWorld
    self.location_rules: Dict[str, Callable[[CollectionState], bool]]
    self.region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: RobobeatWorld):
        self.player = world.player
        self.world = world
        self.location_rules = {}
        self.region_rules = {
            "The Old Passage": self.armory_access,
            "The Citadel": self.study_access,
            "The Machine": self.frazzer_access,
        }
        self.location_rules = {
            "Parkour Room Blueprint": self.shop_access,
            "Curveball Blueprint": self.parkour_access,
            "Stab Blueprint": self.has_contact
        }

    def armory_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=1)

    def study_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=2)

    def frazzer_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=3)

    def shop_access(self, state: CollectionState) -> bool:
        return state.has("Shop Room Blueprint", self.player)

    def parkour_access(self, state: CollectionState) -> bool:
        return state.has("Parkour Room Blueprint", self.player)

    def has_contact(self, state: CollectionState) -> bool:
        return state.has("Contact Blueprint", self.player)

    def set_all_rules(self) -> None:
        multiworld = self.world.multiworld

        for region in multiworld.get_regions(self.player):
            for entrance in region.entrances:
                entrance.access_rule = self.region_rules[region.name]

            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]

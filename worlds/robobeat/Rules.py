from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import RobobeatWorld
else:
    RobobeatWorld = object


class RobobeatRules:
    player: int
    world: RobobeatWorld





    def has_armory_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=1)

    def has_study_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=2)

    def has_frazzer_access(self, state: CollectionState) -> bool:
        return state.has("Progressive Key", self.player, count=3)

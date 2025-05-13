from worlds.AutoWorld import World
from .Options import RobobeatOptions
from .Items import all_items, RobobeatItem, filler_items
from .Locations import all_locations



class RobobeatWorld(World):
    """Rhythm FPS - plz finish"""
    game = "ROBOBEAT"
    origin_region_name = "The HUB"
    options_dataclass = RobobeatOptions
    options: RobobeatOptions
    settings: typing.ClassVar[RobobeatOptions]
    item_name_to_id = {item["name"]: i + 1 for i, item in enumerate(all_items)}
    location_name_to_id = {location: i + 1 for i, location in enumerate(all_locations)}

    def get_filler_item_name(self) -> None:
        return self.random.choice(filler_items)

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_info = all_items[item_id - 1]
        return RobobeatItem(name, item_info['type'], item_id, self.player)


    def create_items(self) -> None:
        num_items_added = 0
        for item in all_items:
            for _ in range(item['count']):
                i = self.create_item(item['name'])
                self.multiworld.itempool.append(i)
                num_items_added += 1

        filler_count = len(all_locations) - num_items_added

        for i in range(filler_count):
            filler_item = self.create_item(self.get_filler_item_name())
            self.multiworld.itempool.append(filler_item)

from worlds.AutoWorld import World
from BaseClasses import ItemClassification, Item, Location, Region
from .Options import RobobeatOptions
from .Items import main_items, blueprint_items, RobobeatItem, filler_items
from .Locations import all_locations, location_regions, RobobeatLocation
from .Regions import all_regions
from . import Rules



class RobobeatWorld(World):
    """Rhythm FPS - plz finish"""
    game = "ROBOBEAT"
    origin_region_name = "The HUB"
    options_dataclass = RobobeatOptions
    options: RobobeatOptions
    all_items = main_items + blueprint_items
    item_name_to_id = {item["name"]: i + 1 for i, item in enumerate(main_items + blueprint_items)}  
    location_name_to_id = {location: i + 1 for i, location in enumerate(all_locations)}

    def generate_early(self) -> None:
        selected_items = []
        if self.options.randomize_starting_loadout.value:
            all_weapons = [item['blueprint_item'] for item in blueprint_items if item['blueprint_type'] == "Weapon"]
            all_utilities = [item['blueprint_item'] for item in blueprint_items if item['blueprint_type'] == "Utility"]
            for _ in range(4):
                item = self.random.choice(all_weapons)
                selected_items.append(item)

            for _ in range(2):
                item = self.random.choice(all_utilities)
                selected_items.append(item)

            self.options.randomized_loadout.value = selected_items
 
    def get_filler_item_name(self) -> None:
        return self.random.choice(filler_items)

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_info = self.all_items[item_id - 1]
        return RobobeatItem(name, item_info['type'], item_id, self.player)

    def create_event(self, name: str) -> Item:
        return RobobeatItem(name, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        num_items_added = 0
        for item in self.all_items:
            if item['name'].endswith("Blueprint"):
                if item['blueprint_item'] in self.options.randomized_loadout.value:
                    continue
            num = 1
            if 'count' in item:
                num = item['count']
            for _ in range(num):
                i = self.create_item(item['name'])
                self.multiworld.itempool.append(i)
                num_items_added += 1

        filler_count = len(all_locations) - num_items_added

        for i in range(filler_count):
            filler_item = self.create_item(self.get_filler_item_name())
            self.multiworld.itempool.append(filler_item)


    def create_regions(self) -> None:
        for region_name in all_regions.keys():
            self.multiworld.regions.append(Region(region_name, self.player, self.multiworld))

        for region_name, region_connections in all_regions.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations({
                location: self.location_name_to_id[location] for location in location_regions[region_name]
            }, RobobeatLocation)
        machine = self.multiworld.get_region("The Machine", self.player)
        win_loc = RobobeatLocation(self.player, "Defeat Frazzer", None, machine)
        win_loc.place_locked_item(self.create_event("Victory"))
        machine.locations.append(win_loc)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def set_rules(self) -> None:
        Rules.RobobeatRules(self).set_all_rules()

    def fill_slot_data(self):
        return {
            'random_loadout': self.options.randomized_loadout.value,
            'death_link': self.options.death_link.value
        }

from worlds.AutoWorld import World
from .Options import RobobeatOptions



class RobobeatWorld(World):
    """Rhythm FPS - plz finish"""
    game = "ROBOBEAT"
    options_dataclass = RobobeatOptions
    options: RobobeatOptions
    settings: typing.ClassVar[RobobeatOptions]

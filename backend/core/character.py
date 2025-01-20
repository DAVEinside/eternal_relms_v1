# Character class definition
from dataclasses import dataclass
from typing import List, Dict
from config.settings import STARTING_STATS

@dataclass
class Character:
    name: str
    archetype: str
    level: int = 1
    hp: int = 100
    mp: int = 50
    stats: Dict[str, int] = None
    inventory: List[str] = None
    special_moves: List[str] = None

    def __post_init__(self):
        if self.stats is None:
            self.stats = STARTING_STATS[self.archetype]
        if self.inventory is None:
            self.inventory = ["Health Potion"]
        if self.special_moves is None:
            self.special_moves = self._get_default_moves()

    def _get_default_moves(self):
        if self.archetype == "Determined Shounen Hero":
            return ["Power Strike", "Friendship Boost"]
        elif self.archetype == "Mysterious Mage":
            return ["Fireball", "Arcane Shield"]
        elif self.archetype == "Swift Ninja":
            return ["Shadow Strike", "Smoke Bomb"]
        elif self.archetype == "Noble Warrior":
            return ["Holy Slash", "Divine Protection"]
        elif self.archetype == "Combat Healer":
            return ["Heal Pulse", "Barrier"]
        return ["Basic Attack"]

    def take_damage(self, amount: int):
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int):
        self.hp = min(100, self.hp + amount)

    def use_mp(self, amount: int) -> bool:
        if self.mp >= amount:
            self.mp -= amount
            return True
        return False

    def is_alive(self):
        return self.hp > 0

    def to_dict(self):
        return {
            "name": self.name,
            "archetype": self.archetype,
            "level": self.level,
            "hp": self.hp,
            "mp": self.mp,
            "stats": self.stats,
            "inventory": self.inventory,
            "special_moves": self.special_moves
        }

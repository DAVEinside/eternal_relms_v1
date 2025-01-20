# Game configuration and constants
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHARACTER_ARCHETYPES = [
    "Determined Shounen Hero",
    "Mysterious Mage",
    "Swift Ninja",
    "Noble Warrior",
    "Combat Healer"
]

COMBAT_ACTIONS = [
    "attack",
    "defend",
    "special_move",
    "item"
]

STARTING_STATS = {
    "Determined Shounen Hero": {"strength": 12, "agility": 10, "intelligence": 8, "defense": 10},
    "Mysterious Mage": {"strength": 6, "agility": 8, "intelligence": 14, "defense": 8},
    "Swift Ninja": {"strength": 8, "agility": 14, "intelligence": 10, "defense": 8},
    "Noble Warrior": {"strength": 10, "agility": 8, "intelligence": 8, "defense": 14},
    "Combat Healer": {"strength": 8, "agility": 10, "intelligence": 12, "defense": 10}
}
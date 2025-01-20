# Combat system
import random
from typing import List, Dict, Tuple
from .character import Character

class CombatSystem:
    def __init__(self, player: Character, enemies: List[Character]):
        self.player = player
        self.enemies = enemies
        self.turn = 0

    def calculate_damage(self, attacker: Character, defender: Character, move_type: str = "normal") -> int:
        base_damage = attacker.stats["strength"] * random.uniform(0.8, 1.2)
        
        if move_type == "special":
            base_damage *= 1.5
        
        defense = defender.stats["defense"]
        return max(1, int(base_damage - defense * 0.5))

    def process_turn(self, action: str, target_idx: int = 0) -> Dict[str, any]:
        if not self.enemies[target_idx].is_alive():
            return {
                "success": False,
                "message": "Target is already defeated!",
                "damage": 0
            }

        result = {
            "success": True,
            "message": "",
            "damage": 0
        }

        # Process player action
        if action == "attack":
            damage = self.calculate_damage(self.player, self.enemies[target_idx])
            self.enemies[target_idx].take_damage(damage)
            result.update({
                "damage": damage,
                "message": f"{self.player.name} attacks for {damage} damage!"
            })

        elif action == "special_move":
            if self.player.use_mp(20):
                damage = self.calculate_damage(self.player, self.enemies[target_idx], "special")
                self.enemies[target_idx].take_damage(int(damage))
                result.update({
                    "damage": damage,
                    "message": f"{self.player.name} uses {self.player.special_moves[0]} for {damage} damage!"
                })
            else:
                result.update({
                    "success": False,
                    "message": "Not enough MP!"
                })

        self.turn += 1
        return result
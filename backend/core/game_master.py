# Main game logic controller
from typing import Dict, Any
from .character import Character
from .combat import CombatSystem
from .story_generator import StoryGenerator

class GameMaster:
    def __init__(self):
        self.story_generator = StoryGenerator()
        self.player = None
        self.current_location = "Starting Village"
        self.game_state = "exploration"
        self.combat_system = None

    def create_character(self, name: str, archetype: str) -> Character:
        self.player = Character(name=name, archetype=archetype)
        return self.player

    def start_combat(self, enemy_name: str = "Mysterious Enemy") -> Dict[str, Any]:
        enemy = Character(name=enemy_name, archetype="Swift Ninja")
        self.combat_system = CombatSystem(self.player, [enemy])
        self.game_state = "combat"
        return {
            "message": f"Combat started with {enemy_name}!",
            "enemy": enemy.to_dict()
        }

    def process_input(self, user_input: str) -> Dict[str, Any]:
        if self.game_state == "exploration":
            # Check for combat trigger words
            if any(word in user_input.lower() for word in ["fight", "attack", "battle"]):
                return self.start_combat()
            
            context = {
                "player_name": self.player.name,
                "player_archetype": self.player.archetype,
                "location": self.current_location,
                "situation": user_input
            }
            story_response = self.story_generator.generate_story_beat(context)
            return {
                "type": "story",
                "content": story_response,
                "character": self.player.to_dict()
            }
        
        elif self.game_state == "combat":
            if not self.combat_system:
                self.game_state = "exploration"
                return {
                    "type": "error",
                    "content": "No active combat"
                }
            
            result = self.combat_system.process_turn(user_input)
            if result["success"]:
                return {
                    "type": "combat",
                    "content": result["message"],
                    "damage": result["damage"],
                    "character": self.player.to_dict()
                }
            
            return {
                "type": "error",
                "content": result["message"]
            }
        
        return {
            "type": "error",
            "content": "Invalid game state"
        }
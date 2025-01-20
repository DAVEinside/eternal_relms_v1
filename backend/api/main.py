# FastAPI entry point
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
from core.game_master import GameMaster

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active games in memory (in production, use a proper database)
active_games = {}

class CharacterCreate(BaseModel):
    name: str
    archetype: str

class GameAction(BaseModel):
    action: str

@app.post("/game/create")
async def create_game():
    game_id = str(len(active_games) + 1)
    active_games[game_id] = GameMaster()
    return {"game_id": game_id}

@app.post("/game/{game_id}/character")
async def create_character(game_id: str, character_data: CharacterCreate):
    if game_id not in active_games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game = active_games[game_id]
    character = game.create_character(character_data.name, character_data.archetype)
    
    return {"character": character.to_dict()}

@app.post("/game/{game_id}/action")
async def process_action(game_id: str, action: GameAction):
    if game_id not in active_games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game = active_games[game_id]
    response = game.process_input(action.action)
    
    return {
        "response": response,
        "game_state": {
            "location": game.current_location,
            "state": game.game_state
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
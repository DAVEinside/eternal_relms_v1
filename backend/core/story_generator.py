# Story generation using LLM
import openai
from typing import Dict
from config.settings import OPENAI_API_KEY

class StoryGenerator:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY

    def generate_story_beat(self, context: Dict) -> str:
        prompt = f"""
        In an anime-style RPG setting:
        Hero: {context['player_name']}, a {context['player_archetype']}
        Current Location: {context['location']}
        Situation: {context['situation']}
        
        Generate a short, dramatic narrative description of what happens next, using anime-style descriptions and incorporating the character's archetype:
        """
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an anime-style RPG game master. Keep responses concise and dramatic."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"As your journey continues... (Error: {str(e)})"

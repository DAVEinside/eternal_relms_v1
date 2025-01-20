// Main app component
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import CharacterCreation from './components/CharacterCreation';
import GameInterface from './components/GameInterface';

const API_BASE_URL = 'http://localhost:8000';

const App = () => {
  const [gameState, setGameState] = useState({
    gameId: null,
    character: null,
    isLoading: true,
  });

  useEffect(() => {
    createGame();
  }, []);

  useEffect(() => {
    console.log("App component loaded");
  }, []);
  

  const createGame = async () => {
    try {
      const response = await axios.post(`${API_BASE_URL}/game/create`);
      setGameState(prev => ({
        ...prev,
        gameId: response.data.game_id,
        isLoading: false,
      }));
    } catch (error) {
      console.error('Error creating game:', error);
    }
  };

  const handleCharacterCreate = async (characterData) => {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/game/${gameState.gameId}/character`,
        characterData
      );
      setGameState(prev => ({
        ...prev,
        character: response.data.character,
      }));
    } catch (error) {
      console.error('Error creating character:', error);
    }
  };

  const handleAction = async (action) => {
    try {
      const response = await axios.post(
        `${API_BASE_URL}/game/${gameState.gameId}/action`,
        { action }
      );
      
      // Update character state if it changed
      if (response.data.response.character) {
        setGameState(prev => ({
          ...prev,
          character: response.data.response.character,
        }));
      }
      
      return response.data;
    } catch (error) {
      console.error('Error processing action:', error);
      return {
        response: {
          type: 'error',
          content: 'Something went wrong. Please try again.',
        },
      };
    }
  };

  if (gameState.isLoading) {
    return <div className="h-screen flex items-center justify-center">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {!gameState.character ? (
        <CharacterCreation onCharacterCreate={handleCharacterCreate} />
      ) : (
        <GameInterface character={gameState.character} onAction={handleAction} />
      )}
    </div>
  );
};

export default App;
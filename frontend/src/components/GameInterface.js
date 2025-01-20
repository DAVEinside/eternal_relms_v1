// Game interface component
import React, { useState, useRef, useEffect } from 'react';
import { HeartPulse, Zap, Sword, Shield, MessageSquare } from 'lucide-react';
import { Card, CardHeader, CardContent, CardTitle } from './ui/card';

const GameInterface = ({ character, onAction }) => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([
    { type: 'system', content: 'Welcome to your adventure! What would you like to do?' }
  ]);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessage = { type: 'player', content: input };
    setMessages(prev => [...prev, newMessage]);
    onAction(input).then(response => {
      setMessages(prev => [...prev, { type: 'system', content: response.response.content }]);
    });
    setInput('');
  };

  const CharacterStats = () => (
    <Card className="mb-4">
      <CardHeader>
        <CardTitle className="flex items-center gap-2">
          <MessageSquare className="w-5 h-5" />
          {character.name} - {character.archetype}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          <div className="flex items-center gap-2">
            <HeartPulse className="text-red-500" />
            <span>HP: {character.hp}/100</span>
          </div>
          <div className="flex items-center gap-2">
            <Zap className="text-blue-500" />
            <span>MP: {character.mp}/50</span>
          </div>
          <div className="flex items-center gap-2">
            <Sword className="text-orange-500" />
            <span>STR: {character.stats.strength}</span>
          </div>
          <div className="flex items-center gap-2">
            <Shield className="text-green-500" />
            <span>DEF: {character.stats.defense}</span>
          </div>
        </div>
      </CardContent>
    </Card>
  );

  return (
    <div className="h-screen flex flex-col p-4 bg-gray-50">
      <CharacterStats />
      
      <Card className="flex-1 mb-4">
        <CardHeader>
          <CardTitle>Adventure Log</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-[calc(100vh-300px)] overflow-y-auto space-y-4">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`p-3 rounded-lg ${
                  message.type === 'player'
                    ? 'bg-blue-100 ml-4'
                    : 'bg-gray-100 mr-4'
                }`}
              >
                {message.content}
              </div>
            ))}
            <div ref={messagesEndRef} />
          </div>
        </CardContent>
      </Card>

      <form onSubmit={handleSubmit} className="flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="What would you like to do?"
          className="flex-1 p-2 border rounded-md"
        />
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded-md hover:bg-blue-700 transition-colors"
        >
          Send
        </button>
      </form>
    </div>
  );
};

export default GameInterface;
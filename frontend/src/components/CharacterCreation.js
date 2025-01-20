import React, { useState } from 'react';
import { Star, Zap, Sword, Shield, HeartPulse } from 'lucide-react';
import { Card, CardHeader, CardContent, CardTitle } from './ui/card';
import { CardDescription } from './ui/card';


const CharacterCreation = ({ onCharacterCreate }) => {
  const [formData, setFormData] = useState({
    name: '',
    archetype: 'Determined Shounen Hero'
  });

  const archetypes = [
    { name: "Determined Shounen Hero", icon: Star, description: "A brave hero with unwavering determination" },
    { name: "Mysterious Mage", icon: Zap, description: "A powerful spellcaster with arcane knowledge" },
    { name: "Swift Ninja", icon: Sword, description: "A quick and agile warrior of the shadows" },
    { name: "Noble Warrior", icon: Shield, description: "A stalwart defender with unwavering honor" },
    { name: "Combat Healer", icon: HeartPulse, description: "A skilled medic with combat abilities" }
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    onCharacterCreate(formData);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-4">
      <Card className="w-full max-w-2xl">
        <CardHeader>
          <CardTitle className="text-2xl">Create Your Character</CardTitle>
          <CardDescription>Begin your anime adventure</CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label className="block text-sm font-medium mb-2">Character Name</label>
              <input
                type="text"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                className="w-full p-2 border rounded-md"
                required
                minLength={2}
              />
            </div>

            <div>
              <label className="block text-sm font-medium mb-2">Choose Your Archetype</label>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {archetypes.map(({ name, icon: Icon, description }) => (
                  <div
                    key={name}
                    className={`p-4 border rounded-lg cursor-pointer transition-colors ${
                      formData.archetype === name ? 'border-blue-500 bg-blue-50' : 'hover:border-gray-300'
                    }`}
                    onClick={() => setFormData({ ...formData, archetype: name })}
                  >
                    <div className="flex items-center gap-3">
                      <Icon className="w-5 h-5" />
                      <div>
                        <h3 className="font-medium">{name}</h3>
                        <p className="text-sm text-gray-500">{description}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-2 px-4 rounded-md hover:bg-blue-700 transition-colors"
            >
              Begin Adventure
            </button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default CharacterCreation;
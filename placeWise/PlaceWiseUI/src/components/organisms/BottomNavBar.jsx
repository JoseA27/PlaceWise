import React, { useState } from 'react';
import { FaHome, FaSearch, FaPlusCircle, FaRegHeart, FaUserCircle } from 'react-icons/fa';

const BottomNavBar = ({ onOptionSelect }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <nav className="fixed bottom-0 left-0 w-full bg-white border-t border-gray-300 z-50">
      <div className="flex justify-around items-center py-2">
        {/* Botón para mostrar el menú de agregar */}
        <button onClick={toggleMenu} className="flex flex-col items-center text-gray-600 hover:text-black">
          <FaPlusCircle className="text-3xl text-blue-500" />
          <span className="text-xs">Agregar</span>
        </button>
      </div>

      {/* Menú desplegable para el botón de agregar */}
      {isMenuOpen && (
        <div className="absolute bottom-12 w-full flex justify-center">
          <div className="bg-white rounded-lg shadow-lg flex flex-col items-center p-2 space-y-2">
            <button onClick={() => onOptionSelect('Fotos')} className="bg-white p-2 rounded-full hover:bg-gray-100 flex items-center space-x-2">
              <FaHome className="text-blue-500" />
              <span>Fotos</span>
            </button>
            <button onClick={() => onOptionSelect('Videos')} className="bg-white p-2 rounded-full hover:bg-gray-100 flex items-center space-x-2">
              <FaSearch className="text-green-500" />
              <span>Videos</span>
            </button>
            <button onClick={() => onOptionSelect('Documentos')} className="bg-white p-2 rounded-full hover:bg-gray-100 flex items-center space-x-2">
              <FaRegHeart className="text-orange-500" />
              <span>Documentos</span>
            </button>
            <button onClick={() => onOptionSelect('Planos')} className="bg-white p-2 rounded-full hover:bg-gray-100 flex items-center space-x-2">
              <FaUserCircle className="text-purple-500" />
              <span>Planos</span>
            </button>
            <button onClick={() => onOptionSelect('Experiencias')} className="bg-white p-2 rounded-full hover:bg-gray-100 flex items-center space-x-2">
              <FaUserCircle className="text-red-500" />
              <span>Experiencias</span>
            </button>
          </div>
        </div>
      )}
    </nav>
  );
};

export default BottomNavBar;
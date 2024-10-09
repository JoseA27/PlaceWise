// src/components/molecules/UserMenu.jsx

import React, { useState } from "react";
import { FaUser, FaCog, FaEnvelope, FaQuestionCircle, FaSignOutAlt } from "react-icons/fa";

const UserMenu = () => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <div className="relative">
      <button
        onClick={toggleDropdown}
        className="flex items-center space-x-2 text-gray-700 hover:text-blue-600 transition duration-300 focus:outline-none"
        aria-label="User profile"
        aria-haspopup="true"
        aria-expanded={isDropdownOpen}
      >
        <FaUser className="text-xl" />
        <span className="hidden md:inline">Perfil</span>
      </button>
      {isDropdownOpen && (
        <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-10">
          {[
            { text: "Configuración", icon: FaCog },
            { text: "Contacto", icon: FaEnvelope },
            { text: "Ayuda", icon: FaQuestionCircle },
            { text: "Cerrar Sesión", icon: FaSignOutAlt },
          ].map((item, index) => (
            <a
              key={index}
              href="#"
              className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 flex items-center"
            >
              <item.icon className="mr-2" /> {item.text}
            </a>
          ))}
        </div>
      )}
    </div>
  );
};

export default UserMenu;

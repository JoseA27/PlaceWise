// src/components/molecules/NavLinks.jsx

import React from "react";

const NavLinks = () => (
  <nav className="hidden md:block">
    <ul className="flex space-x-6">
      {["Inicio", "Propiedades", "Promotores", "Sobre Nosotros"].map((text, index) => (
        <li key={index}>
          <a
            href="#"
            className="text-gray-700 hover:text-blue-600 transition duration-300"
            aria-label={text}
          >
            {text}
          </a>
        </li>
      ))}
    </ul>
  </nav>
);

export default NavLinks;

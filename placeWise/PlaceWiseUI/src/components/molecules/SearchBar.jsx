// src/components/molecules/SearchBar.jsx

import React from "react";
import { FaSearch } from "react-icons/fa";

const SearchBar = () => (
  <div className="relative">
    <input
      type="text"
      placeholder="Buscar propiedades"
      className="bg-gray-100 rounded-full py-2 px-4 focus:outline-none focus:ring-2 focus:ring-blue-400 w-64"
      aria-label="Buscar propiedades"
    />
    <FaSearch className="absolute right-3 top-3 text-gray-400" />
  </div>
);

export default SearchBar;

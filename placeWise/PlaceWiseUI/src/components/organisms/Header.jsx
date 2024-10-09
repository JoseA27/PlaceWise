// src/components/organisms/Header.jsx

import React from "react";
import Logo from "../atoms/Logo";
import NavLinks from "../molecules/NavLinks";
import SearchBar from "../molecules/SearchBar";
import UserMenu from "../molecules/UserMenu";

const Header = () => (
  <header className="bg-[#dedcd6] shadow-md">
    <div className="container mx-auto px-4 py-3">
      <div className="flex flex-col md:flex-row items-center justify-between">
        <div className="flex items-center mb-4 md:mb-0">
          <Logo />
          <NavLinks />
        </div>
        <div className="flex items-center space-x-4">
          <SearchBar />
          <UserMenu />
        </div>
      </div>
    </div>
  </header>
);

export default Header;
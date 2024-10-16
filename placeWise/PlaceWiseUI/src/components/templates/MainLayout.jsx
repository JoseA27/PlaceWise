// src/components/templates/MainLayout.js
import React from 'react';
import Header from '../organisms/Header';

const MainLayout = ({ children }) => {
  return (
    <div className="bg-white">
      <Header />
      <main className="pt-16"> 
        {children}
      </main>
    </div>
  );
};

export default MainLayout;


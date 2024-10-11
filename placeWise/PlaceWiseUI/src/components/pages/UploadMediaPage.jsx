// src/components/pages/UploadMediaPage.jsx

import React from 'react';
import MainLayout from '../templates/MainLayout';
import FileUploadTemplate from '../templates/FileUploadTemplate';
import BottomNavBar from '../organisms/BottomNavBar';

const UploadMediaPage = () => {
  const handleOptionSelect = (option) => {
    console.log(`Selected option: ${option}`);
    // Aquí puedes definir la lógica para manejar cada tipo de archivo.
  };


  return (
    <MainLayout>
      <div className="flex justify-center">
        <h1 className="mt-5 text-xl font-bold text-gray-900">Agregar Media</h1>
      </div>
      <div className="m-10 h-screen">
        <FileUploadTemplate />
      </div>
      <BottomNavBar />
    </MainLayout>
  );
};

export default UploadMediaPage;

// src/components/pages/UploadMediaPage.jsx

import React from 'react';
import MainLayout from '../templates/MainLayout';

import FileUploadTemplate from '../templates/FileUploadTemplate';

const UploadMediaPage = () => {
  return (
    <MainLayout>
      <h1 className="mt-5 m-10 mb-10 text-xl font-bold text-gray-900 dark:text-white">Agregar Media de Propiedad</h1>
      <div className="m-10 h-screen">
        <FileUploadTemplate />
      </div>
    </MainLayout>
  );
};

export default UploadMediaPage;

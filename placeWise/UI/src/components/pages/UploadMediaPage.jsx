// src/components/pages/UploadMediaPage.jsx

import React from 'react';
import MainLayout from '../templates/MainLayout';
import PropertyFormTemplate from '../templates/PropertyFormTemplate';
import FileUploadTemplate from '../templates/FileUploadTemplate';

const UploadMediaPage = () => {
  return (
    <MainLayout>
      <h1 className="mt-5 ml-20 mb-10 text-xl font-bold text-gray-900 dark:text-white">Subir Propiedad</h1>
      <div className="grid grid-cols-2 h-screen">
        <PropertyFormTemplate />
        <FileUploadTemplate />
      </div>
    </MainLayout>
  );
};

export default UploadMediaPage;

// src/components/pages/UploadMediaPage.jsx

import React from 'react';
import MainLayout from '../templates/MainLayout';

import FileUploadTemplate from '../templates/FileUploadTemplate';

const UploadMediaPage = () => {
  return (
    <MainLayout>
      <div className="flex justify-center">
        <h1 className="mt-5 text-xl font-bold text-gray-900">Agregar Media</h1>
      </div>
      <div className="m-10 h-screen">
        <FileUploadTemplate />
      </div>
    </MainLayout>
  );
};

export default UploadMediaPage;

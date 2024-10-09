import React from 'react';
import MainLayout from '../templates/MainLayout';
import PropertyFormTemplate from '../templates/PropertyFormTemplate';
import UploadMediaButton from '../atoms/UploadMediaButton';

const UploadMediaPage = () => {
  return (
    <MainLayout>
        <h1 className="mt-5 ml-20 mb-10 text-xl font-bold text-gray-900 dark:text-white">Subir Propiedad</h1>
        
        <div className="h-screen flex flex-col">
            <div className="justify-center">
            <PropertyFormTemplate />
            </div>
            <div className="flex-1 flex items-center justify-center">
            <UploadMediaButton />
            </div>
        </div>
    </MainLayout>
  );
};

export default UploadMediaPage;
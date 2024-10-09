import React from 'react';
import MainLayout from '../templates/MainLayout';
import PropertyFormTemplate from '../templates/PropertyFormTemplate';
import UploadMediaButton from '../atoms/UploadMediaButton';
import SaveButton from '../atoms/SaveButton';
import CancelButton from '../atoms/CancelButton';

const UploadProperty = () => {
  return (
    <MainLayout>
        <div className="flex justify-center">
          <h1 className="mt-5 mb-10 text-xl font-bold text-gray-900">Subir Propiedad</h1>
        </div>
        <div className="h-screen">
            <PropertyFormTemplate />
            <div className="flex-1 flex items-center justify-center">
              <CancelButton/>
              <UploadMediaButton/>
              <SaveButton/>
            </div>
        </div>
    </MainLayout>
  );
};

export default UploadProperty;
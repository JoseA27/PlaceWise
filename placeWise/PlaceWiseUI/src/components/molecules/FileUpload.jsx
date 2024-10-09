// src/components/molecules/FileUpload.jsx

import React from 'react';
import Dropzone from '../atoms/Dropzone';

const FileUpload = () => {
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      console.log('Archivo seleccionado:', file);
    }
  };

  return (
    <div className="flex items-center justify-center w-full">
      <Dropzone onChange={handleFileChange} />
    </div>
  );
};

export default FileUpload;


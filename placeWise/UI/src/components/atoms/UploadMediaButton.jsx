// src/components/atoms/UploadMediaButton.jsx

import React from 'react';
import { useHistory } from 'react-router-dom';

const UploadMediaButton = () => {
  const handleClick = () => {
    
  };

  return (
    <button
      onClick={handleClick}
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Agregar Media
    </button>
  );
};

export default UploadMediaButton;

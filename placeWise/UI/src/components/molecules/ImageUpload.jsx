// src/components/molecules/ImageUpload.jsx

import React, { useState } from 'react';

const ImageUpload = () => {
  const [images, setImages] = useState([]);

  // Maneja la carga de una nueva imagen
  const handleImageChange = (event) => {
    const files = Array.from(event.target.files);
    const newImages = files.map((file) => URL.createObjectURL(file));
    setImages((prevImages) => [...prevImages, ...newImages]);
  };

  return (
    <div className="flex flex-col space-y-4 mt-4">
      <div className="flex flex-wrap space-x-4">
        {images.map((image, index) => (
          <div key={index} className="relative w-24 h-24 border border-gray-300 mb-4">
            <img src={image} alt={`Cargada ${index}`} className="object-cover w-full h-full" />
          </div>
        ))}
        <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mb-4">
          <input
            type="file"
            onChange={handleImageChange}
            className="hidden"
            accept="image/*"
          />
          <span className="text-xl text-gray-500">+</span>
        </label>
      </div>
    </div>
  );
};

export default ImageUpload;

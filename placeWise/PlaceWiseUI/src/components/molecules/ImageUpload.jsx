// src/components/molecules/ImageUpload.jsx

import React, { useState } from 'react';

const ImageUpload = () => {
  const [images, setImages] = useState([]);

  const handleImageChange = (event) => {
    const files = Array.from(event.target.files);
    const newImages = files.map((file) => URL.createObjectURL(file));
    setImages((prevImages) => [...prevImages, ...newImages]);
  };

  return (
    <div className="flex flex-col space-y-4 mt-4">
      {/* Contenedor responsivo para scroll horizontal */}
      <div className="flex space-x-4 overflow-x-auto snap-x snap-mandatory custom-scrollbar md:flex-nowrap md:w-full w-screen">
        {images.map((image, index) => (
          <div key={index} className="relative flex-shrink-0 w-32 h-32 md:w-24 md:h-24 border border-gray-300 snap-center">
            <img src={image} alt={`Cargada ${index}`} className="object-cover w-full h-full" />
          </div>
        ))}
        <label className="flex-shrink-0 w-32 h-32 md:w-24 md:h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer snap-center">
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

// src/components/molecules/ImageUpload.jsx

import React, { useState } from 'react';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const ImageUpload = () => {
  const [images, setImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  // Maneja la carga de una nueva imagen
  const handleImageChange = (event) => {
    const files = Array.from(event.target.files);
    const newImages = files.map((file) => URL.createObjectURL(file));
    setImages((prevImages) => [...prevImages, ...newImages]);
    setCurrentIndex(images.length); // Muestra la última imagen agregada
  };

  // Función para cambiar a la imagen anterior
  const prevImage = () => {
    setCurrentIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
  };

  // Función para cambiar a la siguiente imagen
  const nextImage = () => {
    setCurrentIndex((prevIndex) => (prevIndex === images.length - 1 ? 0 : prevIndex + 1));
  };

  const swipeHandlers = useSwipeable({
    onSwipedLeft: () => nextImage(),
    onSwipedRight: () => prevImage(),
    preventDefaultTouchmoveEvent: true,
    trackMouse: true,
  });

  return (
    <div className="flex flex-col items-center space-y-4 mt-4">
      {/* Carrusel de imágenes grandes */}
      {images.length > 0 && (
        <div className="relative w-full h-64 flex justify-center items-center overflow-hidden" {...swipeHandlers}>
          <button onClick={prevImage} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>
          <img
            src={images[currentIndex]}
            alt={`Propiedad ${currentIndex}`}
            className="object-contain w-auto h-full"
          />
          <button onClick={nextImage} className="absolute right-0 p-2 text-gray-600 hover:text-black">
          <FaChevronRight />
          </button>

          {/* Indicadores de imagenes */}
          <div className="absolute bottom-2 flex space-x-1">
            {images.map((_, index) => (
              <div
                key={index}
                className={`w-2 h-2 rounded-full ${currentIndex === index ? 'bg-gray-100' : 'bg-gray-400'}`}
              ></div>
            ))}
          </div>
        </div>
      )}

      {/* Botón para agregar imágenes */}
      <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mt-4">
        <input
          type="file"
          onChange={handleImageChange}
          className="hidden"
          accept="image/*"
          multiple
        />
        <span className="text-xl text-gray-500">+</span>
      </label>
    </div>
  );
};

export default ImageUpload;

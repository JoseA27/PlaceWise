// src/components/molecules/ImageUpload.jsx

import React, { useState } from 'react';
import { FaChevronLeft, FaChevronRight, FaImage } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const ImageUpload = ({ images = [] }) => { 
  const [currentIndex, setCurrentIndex] = useState(0);
  const [animationClass, setAnimationClass] = useState('');

  const prevImage = () => {
    setAnimationClass('animate-slideOutLeft');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === 0 ? images.length - 1 : prevIndex - 1));
      setAnimationClass('animate-slideInLeft');
    }, 250); // Ajusta el tiempo para sincronizar con la animación
  };

  const nextImage = () => {
    setAnimationClass('animate-slideOutRight');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === images.length - 1 ? 0 : prevIndex + 1));
      setAnimationClass('animate-slideInRight');
    }, 250);
  };

  const swipeHandlers = useSwipeable({
    onSwipedLeft: nextImage,
    onSwipedRight: prevImage,
    preventDefaultTouchmoveEvent: true,
    trackMouse: true,
  });

  return (
    <div className="flex flex-col items-center space-y-4 mt-4">
      {images.length === 0 ? (
        <div className="w-full h-64 border border-gray-300 flex flex-col items-center justify-center bg-gray-100">
          <FaImage className="text-gray-400 text-6xl" />
          <p className="mt-2 text-gray-500">No hay imágenes</p>
        </div>
      ) : (
        <div 
          className="relative w-full h-64 flex justify-center items-center overflow-hidden" 
          {...swipeHandlers}
        >
          <button onClick={prevImage} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>
          <img 
            src={images[currentIndex]} 
            alt={`Propiedad ${currentIndex}`} 
            className={`object-contain w-auto h-full ${animationClass}`} 
          />
          <button onClick={nextImage} className="absolute right-0 p-2 text-gray-600 hover:text-black">
            <FaChevronRight />
          </button>
          <div className="absolute bottom-2 flex space-x-1">
            {images.map((_, index) => (
              <div
                key={index}
                className={`w-1 h-1 rounded-full ${currentIndex === index ? 'bg-gray-100' : 'bg-gray-400'}`}
              ></div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default ImageUpload;

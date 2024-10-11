import React, { useState } from 'react';

const InstagramCarousel = ({ images }) => {
  return (
    <div className="relative w-full flex overflow-x-scroll snap-x snap-mandatory scrollbar-hide">
      {images.map((image, index) => (
        <div key={index} className="flex-shrink-0 snap-center w-full sm:w-auto">
          <img
            src={image}
            alt={`Imagen ${index}`}
            className="w-full h-auto object-cover"
          />
        </div>
      ))}
    </div>
  );
};

export default InstagramCarousel;

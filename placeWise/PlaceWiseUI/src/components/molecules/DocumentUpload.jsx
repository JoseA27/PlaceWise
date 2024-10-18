// src/components/molecules/DocumentUpload.jsx

import React, { useState } from 'react';
import { FaFileAlt, FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const DocumentUpload = ({ documents = [] }) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [animationClass, setAnimationClass] = useState('');

  const handleDocumentChange = (event) => {
    const files = Array.from(event.target.files);
    const newDocuments = files.map((file) => ({
      url: URL.createObjectURL(file),
      name: file.name,
    }));
    setDocuments((prevDocuments) => [...prevDocuments, ...newDocuments]);
    setCurrentIndex(documents.length);
  };

  const prevDocument = () => {
    setAnimationClass('animate-slideOutLeft');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === 0 ? documents.length - 1 : prevIndex - 1));
      setAnimationClass('animate-slideInLeft');
    }, 250);
  };

  const nextDocument = () => {
    setAnimationClass('animate-slideOutRight');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === documents.length - 1 ? 0 : prevIndex + 1));
      setAnimationClass('animate-slideInRight');
    }, 250);
  };

  const swipeHandlers = useSwipeable({
    onSwipedLeft: () => nextDocument(),
    onSwipedRight: () => prevDocument(),
    preventDefaultTouchmoveEvent: true,
    trackMouse: true,
  });

  return (
    <div className="flex flex-col items-center space-y-4 mt-4">
      {documents.length === 0 ? (
        <div className="w-full h-48 border border-gray-300 flex flex-col items-center justify-center bg-gray-100 p-4">
          <FaFileAlt className="text-gray-400 text-6xl" />
          <p className="mt-2 text-gray-500 text-center">No hay documentos</p>
        </div>
      ) : (
        <div
          className="relative w-48 h-48 border border-gray-300 flex items-center justify-center bg-gray-100 overflow-hidden p-4"
          {...swipeHandlers}
        >
          <button onClick={prevDocument} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>

          <div className={`flex flex-col items-center justify-center ${animationClass}`}>
            <FaFileAlt className="text-gray-700 text-6xl" />
            <div className="absolute bottom-0 w-full bg-gray-800 bg-opacity-75 text-white text-xs text-center p-1 truncate">
              {documents[currentIndex].name}
            </div>
          </div>

          <button onClick={nextDocument} className="absolute right-0 p-2 text-gray-600 hover:text-black">
            <FaChevronRight />
          </button>

          {/* Indicadores de posición (puntos) */}
          <div className="absolute bottom-4 flex space-x-1">
            {documents.map((_, index) => (
              <div
                key={index}
                className={`w-2 h-2 rounded-full ${index === currentIndex ? 'bg-gray-800' : 'bg-gray-300'}`}
              ></div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default DocumentUpload;

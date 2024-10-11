// src/components/molecules/DocumentUpload.jsx

import React, { useState } from 'react';
import { FaFileAlt, FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const DocumentUpload = () => {
  const [documents, setDocuments] = useState([]);
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
    setAnimationClass('animate-slideOutRight');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === 0 ? documents.length - 1 : prevIndex - 1));
      setAnimationClass('animate-slideInRight');
    }, 250);
  };

  const nextDocument = () => {
    setAnimationClass('animate-slideOutLeft');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === documents.length - 1 ? 0 : prevIndex + 1));
      setAnimationClass('animate-slideInLeft');
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
      {documents.length > 0 && (
        <div
          className="relative w-32 h-32 border border-gray-300 flex items-center justify-center bg-gray-100 overflow-hidden"
          {...swipeHandlers}
        >
          <button onClick={prevDocument} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>

          <div className={`flex flex-col items-center justify-center ${animationClass}`}>
            <FaFileAlt className="text-gray-700 text-5xl" />
            <div className="absolute bottom-0 w-full bg-gray-800 bg-opacity-75 text-white text-xs text-center p-1 truncate">
              {documents[currentIndex].name}
            </div>
          </div>

          <button onClick={nextDocument} className="absolute right-0 p-2 text-gray-600 hover:text-black">
            <FaChevronRight />
          </button>

          <div className="absolute bottom-4 flex space-x-1">
            {documents.map((_, index) => (
              <div
                key={index}
                className={`w-2 h-2 rounded-full ${
                  index === currentIndex ? 'bg-gray-800' : 'bg-gray-300'
                }`}
              ></div>
            ))}
          </div>
        </div>
      )}

      <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mt-4">
        <input
          type="file"
          onChange={handleDocumentChange}
          className="hidden"
          accept=".pdf,.doc,.docx,.txt,.xls,.xlsx"
          multiple
        />
        <span className="text-xl text-gray-500">+</span>
      </label>
    </div>
  );
};

export default DocumentUpload;

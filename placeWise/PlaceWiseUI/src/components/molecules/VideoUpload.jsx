// src/components/molecules/VideoUpload.jsx

import React, { useState } from 'react';
import { FaChevronLeft, FaChevronRight, FaVideo } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const VideoUpload = ({ videos = [] }) => { 
  const [currentIndex, setCurrentIndex] = useState(0);
  const [animationClass, setAnimationClass] = useState('');

  const prevVideo = () => {
    setAnimationClass('animate-slideOutLeft');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === 0 ? videos.length - 1 : prevIndex - 1));
      setAnimationClass('animate-slideInLeft');
    }, 250); // Ajusta el tiempo para sincronizar con la animación
  };

  const nextVideo = () => {
    setAnimationClass('animate-slideOutRight');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === videos.length - 1 ? 0 : prevIndex + 1));
      setAnimationClass('animate-slideInRight');
    }, 250);
  };

  const swipeHandlers = useSwipeable({
    onSwipedLeft: nextVideo,
    onSwipedRight: prevVideo,
    preventDefaultTouchmoveEvent: true,
    trackMouse: true,
  });

  return (
    <div className="flex flex-col items-center space-y-4 mt-4">
      {videos.length === 0 ? (
        <div className="w-full h-64 border border-gray-300 flex flex-col items-center justify-center bg-gray-100">
          <FaVideo className="text-gray-400 text-6xl" />
          <p className="mt-2 text-gray-500">No hay videos</p>
        </div>
      ) : (
        <div 
          className="relative w-full h-64 flex justify-center items-center overflow-hidden" 
          {...swipeHandlers}
        >
          <button onClick={prevVideo} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>
          <video 
            src={videos[currentIndex]} 
            className={`object-contain w-auto h-full ${animationClass}`} 
            controls 
            loop 
          />
          <button onClick={nextVideo} className="absolute right-0 p-2 text-gray-600 hover:text-black">
            <FaChevronRight />
          </button>
          <div className="absolute bottom-2 flex space-x-1">
            {videos.map((_, index) => (
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

export default VideoUpload;
